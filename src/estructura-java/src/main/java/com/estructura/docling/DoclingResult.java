/* (C) 2026 Diego Toribio. All rights reserved. */
package com.estructura.docling;

import java.nio.file.Path;
import java.util.List;
import java.util.Objects;

/**
 * Immutable view of the Docling ingestion output coming from the Python runner.
 */
public record DoclingResult(
    boolean doclingObjectCreated,
    String doclingVersion,
    Path inputPath,
    Path markdownPath,
    Path textPath,
    DoclingMetrics metrics,
    List<String> rawOutput
) {
  public DoclingResult {
    Objects.requireNonNull(rawOutput, "rawOutput");
    rawOutput = List.copyOf(rawOutput);
  }

  public boolean hasTranscription() {
    return textPath != null;
  }
}
