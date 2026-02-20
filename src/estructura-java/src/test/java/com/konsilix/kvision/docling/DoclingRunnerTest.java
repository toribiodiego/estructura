/* (C) 2026 Konsilix. All rights reserved. */
package com.konsilix.kvision.docling;

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
    assertNotNull(result.textPath());
    assertTrue(Files.exists(result.textPath()), "Transcription file should exist");
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
    assertTrue(result.hasTranscription());
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
