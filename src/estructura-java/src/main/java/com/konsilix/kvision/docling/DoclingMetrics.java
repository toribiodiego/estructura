/* (C) 2026 Konsilix. All rights reserved. */
package com.konsilix.kvision.docling;

/**
 * Structured metrics emitted by the Python Docling runner.
 */
public record DoclingMetrics(
    Stage docling,
    OcrStage ocr,
    Options options) {

  public record Stage(boolean enabled, Double seconds) {}

  public record OcrStage(boolean enabled, Double seconds, Integer pages, Integer dpi) {}

  public record Options(
      boolean tableStructure,
      boolean imageAnnotations,
      Integer maxPages,
      Integer maxImagePages,
      Integer maxImagesPerPage,
      Integer maxTotalImages,
      boolean cacheUsed) {}
}
