/* (C) 2026 Konsilix. All rights reserved. */
package com.konsilix.estructura.docling;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;

class DoclingRunnerTest {
  private static final String TEST_SCRIPT = "/scripts/fake_docling_runner.py";

  @TempDir Path tempDir;

  @Test
  void ingestParsesSuccessfulOutput() throws Exception {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path input = Files.createTempFile("docling_success", ".pdf");
    Files.writeString(input, "dummy");

    DoclingResult result = runner.ingest(input.toString(), tempDir);

    assertTrue(result.doclingObjectCreated(), "Docling flag should be true");
    assertEquals("test-version", result.doclingVersion());
    assertNotNull(result.inputPath());
    assertTrue(Files.isSameFile(result.inputPath(), input));
    assertNotNull(result.markdownPath());
    assertTrue(Files.exists(result.markdownPath()), "Markdown file should exist");
  }

  @Test
  void ingestThrowsWhenRunnerExitsWithError() throws Exception {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path input = tempDir.resolve("should_exit1.pdf");
    Files.writeString(input, "dummy");

    assertThrows(DoclingRunnerException.class, () -> runner.ingest(input.toString(), tempDir));
  }

  @Test
  void ingestThrowsWhenStatusNotOk() throws IOException {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path input = tempDir.resolve("force_badstatus.pdf");
    Files.writeString(input, "dummy");

    assertThrows(DoclingRunnerException.class, () -> runner.ingest(input.toString(), tempDir));
  }

  @Test
  void ingestRejectsMissingInputFile() {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path missing = tempDir.resolve("missing.pdf");

    assertThrows(DoclingRunnerException.class, () -> runner.ingest(missing.toString(), tempDir));
  }

  @Test
  void ingestAllowsSkippingDoclingStage() throws Exception {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path input = Files.createTempFile("ocr_only", ".pdf");
    Files.writeString(input, "dummy");

    DoclingRunnerOptions options = DoclingRunnerOptions.defaults().withRunDocling(false).withRunOcr(true);

    DoclingResult result = runner.ingest(input.toString(), tempDir, options);

    assertFalse(result.doclingObjectCreated());
    assertFalse(result.hasTranscription(), "No text output in default markdown mode");
  }

  @Test
  void ingestTextOutputProducesTranscription() throws Exception {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path input = Files.createTempFile("text_output", ".pdf");
    Files.writeString(input, "dummy");

    DoclingRunnerOptions options = DoclingRunnerOptions.defaults().withOutputFormat("text");

    DoclingResult result = runner.ingest(input.toString(), tempDir, options);

    assertTrue(result.doclingObjectCreated());
    assertTrue(result.hasTranscription(), "Text output mode should produce transcription");
    assertNotNull(result.textPath());
    assertTrue(Files.exists(result.textPath()), "Transcription file should exist");
  }

  @Test
  void ingestImageCaptureProducesArtifacts() throws Exception {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path input = Files.createTempFile("image_capture", ".pdf");
    Files.writeString(input, "dummy");

    DoclingRunnerOptions options = DoclingRunnerOptions.defaults().withImageCapture(true);

    DoclingResult result = runner.ingest(input.toString(), tempDir, options);

    assertTrue(result.doclingObjectCreated());
    assertNotNull(result.markdownPath());

    Path pagesDir = tempDir.resolve("images").resolve("pages");
    assertTrue(Files.isDirectory(pagesDir), "Page images directory should exist");
    assertTrue(Files.exists(pagesDir.resolve("page_001.png")), "Page 1 image should exist");
    assertTrue(Files.exists(pagesDir.resolve("page_002.png")), "Page 2 image should exist");

    Path cropsDir = tempDir.resolve("images").resolve("crops");
    assertTrue(Files.isDirectory(cropsDir), "Crops directory should exist");
    assertTrue(Files.exists(cropsDir.resolve("p001-01.png")), "Crop p001-01 should exist");
    assertTrue(Files.exists(cropsDir.resolve("p002-01.png")), "Crop p002-01 should exist");

    Path manifest = tempDir.resolve("images").resolve("manifest.txt");
    assertTrue(Files.exists(manifest), "Manifest file should exist");
    String manifestContent = Files.readString(manifest);
    assertTrue(manifestContent.startsWith("# id | page"), "Manifest should have header");
    assertTrue(manifestContent.contains("img-p001-01"), "Manifest should contain first image entry");
    assertTrue(manifestContent.contains("img-p002-01"), "Manifest should contain second image entry");
  }

  @Test
  void ingestAllowsSkippingOcrStage() throws Exception {
    DoclingRunner runner = new DoclingRunner(TEST_SCRIPT);
    Path input = Files.createTempFile("docling_only", ".pdf");
    Files.writeString(input, "dummy");

    DoclingRunnerOptions options = DoclingRunnerOptions.defaults().withRunDocling(true).withRunOcr(false);

    DoclingResult result = runner.ingest(input.toString(), tempDir, options);

    assertTrue(result.doclingObjectCreated());
    assertFalse(result.hasTranscription());
  }
}
