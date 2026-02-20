/* (C) 2026 Konsilix. All rights reserved. */
package com.konsilix.kvision.docling;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.InvalidPathException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

/**
 * Runs the Python Docling ingestion pipeline and returns structured data.
 */
public class DoclingRunner {
  private static final String DEFAULT_RESOURCE = "/scripts/run_docling.py";

  private final String scriptResource;
  private final ObjectMapper mapper;
  private final DoclingRunnerOptions options;

  public DoclingRunner() {
    this(DEFAULT_RESOURCE, DoclingRunnerOptions.defaults());
  }

  public DoclingRunner(DoclingRunnerOptions options) {
    this(DEFAULT_RESOURCE, options);
  }

  DoclingRunner(String scriptResource) {
    this(scriptResource, DoclingRunnerOptions.defaults());
  }

  DoclingRunner(String scriptResource, DoclingRunnerOptions options) {
    this.scriptResource = Objects.requireNonNull(scriptResource, "scriptResource");
    this.options = Objects.requireNonNull(options, "options");
    this.mapper = new ObjectMapper();
  }

  public DoclingResult ingest(String input, Path outputDirectory) throws DoclingRunnerException {
    return ingest(input, outputDirectory, this.options);
  }

  public DoclingResult ingest(String input, Path outputDirectory, DoclingRunnerOptions options)
      throws DoclingRunnerException {
    if (input == null || input.trim().isEmpty()) {
      throw new IllegalArgumentException("input must not be null or blank");
    }

    Path outDir;
    try {
      outDir = resolveOutputDirectory(outputDirectory);
    } catch (IOException e) {
      throw new DoclingRunnerException("Unable to prepare output directory", e);
    }

    final String normalizedInput = normalizeInput(input);
    final DoclingRunnerOptions effectiveOptions = options != null ? options : DoclingRunnerOptions.defaults();

    Path script = null;
    try {
      script = extractScript();
      List<String> command = buildCommand(script, normalizedInput, outDir, effectiveOptions);
      ProcessBuilder pb = new ProcessBuilder(command);
      pb.redirectErrorStream(true);
      Process process = pb.start();

      List<String> outputLines = readProcessOutput(process);
      int exitCode = process.waitFor();
      if (exitCode != 0) {
        String combined =
            outputLines.isEmpty()
                ? "(no output)"
                : outputLines.stream().collect(Collectors.joining(System.lineSeparator()));
        throw new DoclingRunnerException("Docling runner failed with exit code " + exitCode + ":\n" + combined);
      }
      return parseResult(outputLines, effectiveOptions);
    } catch (IOException e) {
      throw new DoclingRunnerException("Failed running Docling ingestion", e);
    } catch (InterruptedException e) {
      Thread.currentThread().interrupt();
      throw new DoclingRunnerException("Interrupted while running Docling ingestion", e);
    } finally {
      if (script != null) {
        try {
          Files.deleteIfExists(script);
        } catch (IOException ignore) {
          // Best effort cleanup.
        }
      }
    }
  }

  private Path resolveOutputDirectory(Path outputDirectory) throws IOException {
    Path outDir = outputDirectory != null ? outputDirectory : Paths.get("out");
    if (!outDir.isAbsolute()) {
      outDir = outDir.toAbsolutePath();
    }
    Files.createDirectories(outDir);
    return outDir;
  }

  private String normalizeInput(String input) throws DoclingRunnerException {
    if (isLikelyUrl(input)) {
      return input;
    }
    Path path;
    try {
      path = Paths.get(input);
    } catch (InvalidPathException e) {
      throw new DoclingRunnerException("Input path is invalid: " + input, e);
    }
    if (!Files.exists(path)) {
      throw new DoclingRunnerException("Input file does not exist: " + path);
    }
    return path.toAbsolutePath().toString();
  }

  private Path extractScript() throws IOException, DoclingRunnerException {
    Path tmpScript = Files.createTempFile("run_docling", ".py");
    try (InputStream in = DoclingRunner.class.getResourceAsStream(scriptResource)) {
      if (in == null) {
        throw new DoclingRunnerException("Python runner resource not found: " + scriptResource);
      }
      Files.copy(in, tmpScript, java.nio.file.StandardCopyOption.REPLACE_EXISTING);
    }
    tmpScript.toFile().setReadable(true);
    return tmpScript;
  }

  private List<String> readProcessOutput(Process process) throws IOException {
    List<String> lines = new ArrayList<>();
    try (BufferedReader reader =
        new BufferedReader(new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8))) {
      String line;
      while ((line = reader.readLine()) != null) {
        lines.add(line);
      }
    }
    return lines;
  }

  private List<String> buildCommand(
      Path script, String normalizedInput, Path outDir, DoclingRunnerOptions options) {
    List<String> command = new ArrayList<>();
    command.add("python3");
    command.add(script.toString());
    command.add(normalizedInput);
    command.add(outDir.toString());

    if (options.dpi() != null) {
      command.add("--dpi");
      command.add(Integer.toString(options.dpi()));
    }
    if (!options.runDocling()) {
      command.add("--no-docling");
    }
    if (!options.runOcr()) {
      command.add("--no-ocr");
    }
    if (options.progress()) {
      command.add("--progress");
    }
    if (options.useCache()) {
      command.add("--use-cache");
    }
    if (options.tableStructure()) {
      command.add("--table-structure");
    }
    if (options.verbose()) {
      command.add("--verbose");
    }
    if (options.maxPages() != null) {
      command.add("--max-pages");
      command.add(Integer.toString(options.maxPages()));
    }
    return command;
  }

  private DoclingResult parseResult(List<String> outputLines, DoclingRunnerOptions options)
      throws DoclingRunnerException {
    boolean doclingCreated = false;
    String doclingVersion = null;
    Path inputPath = null;
    Path markdownPath = null;
    Path textPath = null;
    DoclingMetrics metrics = null;

    for (String line : outputLines) {
      String trimmed = line.trim();
      if (trimmed.isEmpty()) {
        continue;
      }
      JsonNode node = tryParseJson(trimmed);
      if (node == null) {
        continue;
      }

      String event = node.path("event").asText(null);

      if ("docling_object_created".equals(event)) {
        doclingCreated = true;
        doclingVersion = node.path("docling_version").asText(null);
        continue;
      }

      if ("metrics_summary".equals(event)) {
        metrics = parseMetrics(node);
        continue;
      }

      if (node.has("status")) {
        String status = node.path("status").asText();
        if (!"ok".equalsIgnoreCase(status)) {
          throw new DoclingRunnerException("Docling runner returned non-ok status: " + status);
        }
        inputPath = toOptionalPath(node, "input");
        markdownPath = toOptionalPath(node, "markdown");
        textPath = toOptionalPath(node, "text");
      }
    }

    if (options.runDocling() && !doclingCreated) {
      throw new DoclingRunnerException("Docling runner did not report a created document object.");
    }
    return new DoclingResult(doclingCreated, doclingVersion, inputPath, markdownPath, textPath,
        metrics, outputLines);
  }

  private DoclingMetrics parseMetrics(JsonNode node) {
    JsonNode doclingNode = node.path("docling");
    DoclingMetrics.Stage docling = new DoclingMetrics.Stage(
        doclingNode.path("enabled").asBoolean(false),
        toOptionalDouble(doclingNode, "seconds"));

    JsonNode ocrNode = node.path("ocr");
    DoclingMetrics.OcrStage ocr = new DoclingMetrics.OcrStage(
        ocrNode.path("enabled").asBoolean(false),
        toOptionalDouble(ocrNode, "seconds"),
        toOptionalInt(ocrNode, "pages"),
        toOptionalInt(ocrNode, "dpi"));

    JsonNode optionsNode = node.path("options");
    DoclingMetrics.Options opts = new DoclingMetrics.Options(
        optionsNode.path("table_structure").asBoolean(false),
        optionsNode.path("image_annotations").asBoolean(false),
        toOptionalInt(optionsNode, "max_pages"),
        optionsNode.path("cache_used").asBoolean(false));

    return new DoclingMetrics(docling, ocr, opts);
  }

  private Double toOptionalDouble(JsonNode parent, String field) {
    JsonNode value = parent.get(field);
    if (value == null || value.isNull()) {
      return null;
    }
    return value.asDouble();
  }

  private Integer toOptionalInt(JsonNode parent, String field) {
    JsonNode value = parent.get(field);
    if (value == null || value.isNull()) {
      return null;
    }
    return value.asInt();
  }

  private Path toOptionalPath(JsonNode node, String field) {
    JsonNode value = node.get(field);
    if (value == null || value.isNull()) {
      return null;
    }
    String text = value.asText();
    if (text == null || text.isBlank()) {
      return null;
    }
    try {
      Path path = Paths.get(text);
      if (!path.isAbsolute()) {
        return path.normalize();
      }
      return path;
    } catch (InvalidPathException ignore) {
      return null;
    }
  }

  private JsonNode tryParseJson(String line) {
    try {
      return mapper.readTree(line);
    } catch (JsonProcessingException e) {
      return null;
    }
  }

  private boolean isLikelyUrl(String value) {
    String lower = value.toLowerCase();
    return lower.startsWith("http://") || lower.startsWith("https://");
  }
}
