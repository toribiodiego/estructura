/* (C) 2026 Konsilix. All rights reserved. */
package com.konsilix.kvision.docling;

import java.nio.file.InvalidPathException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class DoclingCli {
  public static void main(String[] args) {
    final String input = System.getProperty("doc.input", (args.length > 0 ? args[0] : "")).trim();
    if (input.isEmpty()) {
      throw new IllegalArgumentException("No input provided. Use -Ddoc.input=<url_or_path> or pass as first CLI arg.");
    }
    final String outDir = System.getProperty("doc.out", "out");

    Path outPath;
    try {
      outPath = Paths.get(outDir);
    } catch (InvalidPathException e) {
      throw new IllegalArgumentException("Invalid output directory: " + outDir, e);
    }

    DoclingRunnerOptions options = loadOptionsFromSystemProperties();
    DoclingRunner runner = new DoclingRunner(options);
    try {
      DoclingResult result = runner.ingest(input, outPath);
      if (result.doclingObjectCreated()) {
        System.out.printf("Docling document created (version=%s)%n", result.doclingVersion());
      } else {
        System.out.println("Docling stage skipped by configuration.");
      }
      if (result.hasTranscription()) {
        System.out.println("Transcription path: " + result.textPath());
      }
    } catch (DoclingRunnerException e) {
      System.err.println("Docling ingestion failed: " + e.getMessage());
      if (e.getCause() != null) {
        e.getCause().printStackTrace(System.err);
      }
      System.exit(1);
    }
  }

  private static DoclingRunnerOptions loadOptionsFromSystemProperties() {
    DoclingRunnerOptions opts = DoclingRunnerOptions.defaults();

    String docMode = System.getProperty("doc.mode", "");
    switch (docMode.toLowerCase()) {
      case "docling-only":
        opts = opts.withRunOcr(false).withRunDocling(true).withTableStructure(true).withImageAnnotations(false);
        break;
      case "ocr-only":
        opts = opts.withRunDocling(false).withRunOcr(true).withTableStructure(false).withImageAnnotations(false);
        break;
      case "tables":
        opts = opts.withRunDocling(true).withRunOcr(true).withTableStructure(true).withImageAnnotations(false);
        break;
      case "annotations":
        opts =
            opts.withRunDocling(true)
                .withRunOcr(true)
                .withTableStructure(true)
                .withImageAnnotations(true);
        break;
      default:
        break;
    }

    String doclingProp = System.getProperty("doc.docling");
    if (doclingProp != null) {
      opts = opts.withRunDocling(Boolean.parseBoolean(doclingProp));
    }

    String ocrProp = System.getProperty("doc.ocr");
    if (ocrProp != null) {
      opts = opts.withRunOcr(Boolean.parseBoolean(ocrProp));
    }

    if (Boolean.getBoolean("doc.progress")) {
      opts = opts.withProgress(true);
    }

    if (Boolean.getBoolean("doc.useCache")) {
      opts = opts.withUseCache(true);
    }

    if (Boolean.getBoolean("doc.tableStructure")) {
      opts = opts.withTableStructure(true);
    }

    if (Boolean.getBoolean("doc.imageAnnotations")) {
      opts = opts.withImageAnnotations(true);
    }

    if (Boolean.getBoolean("doc.imageCapture")) {
      opts = opts.withImageCapture(true);
    }

    if (Boolean.getBoolean("doc.verbose")) {
      opts = opts.withVerbose(true);
    }

    String maxPagesProp = System.getProperty("doc.maxPages");
    if (maxPagesProp != null && !maxPagesProp.isBlank()) {
      try {
        opts = opts.withMaxPages(Integer.parseInt(maxPagesProp));
      } catch (NumberFormatException ignore) {
        System.err.println("Ignoring invalid doc.maxPages value: " + maxPagesProp);
      }
    }

    String dpiProp = System.getProperty("doc.dpi");
    if (dpiProp != null && !dpiProp.isBlank()) {
      try {
        opts = opts.withDpi(Integer.parseInt(dpiProp));
      } catch (NumberFormatException ignore) {
        System.err.println("Ignoring invalid doc.dpi value: " + dpiProp);
      }
    }

    String outputProp = System.getProperty("doc.output");
    if (outputProp != null && !outputProp.isBlank()) {
      opts = opts.withOutputFormat(outputProp);
    }

    return opts;
  }
}
