/* (C) 2026 Konsilix. All rights reserved. */
package com.konsilix.kvision.docling;

/**
 * Configuration for DoclingRunner.
 */
public record DoclingRunnerOptions(
    boolean runDocling,
    boolean runOcr,
    boolean progress,
    boolean useCache,
    boolean tableStructure,
    boolean imageAnnotations,
    boolean imageCapture,
    boolean verbose,
    Integer maxPages,
    Integer dpi,
    String outputFormat
) {
  public static DoclingRunnerOptions defaults() {
    return new DoclingRunnerOptions(true, true, false, false, false, false, false, false, null, 120, "markdown");
  }

  public DoclingRunnerOptions withRunDocling(boolean value) {
    return new DoclingRunnerOptions(value, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withRunOcr(boolean value) {
    return new DoclingRunnerOptions(runDocling, value, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withProgress(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, value, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withUseCache(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, value, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withMaxPages(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, value, dpi, outputFormat);
  }

  public DoclingRunnerOptions withDpi(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, value, outputFormat);
  }

  public DoclingRunnerOptions withTableStructure(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, value, imageAnnotations, imageCapture, verbose, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withImageAnnotations(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, value, imageCapture, verbose, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withImageCapture(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, value, verbose, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withVerbose(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, value, maxPages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withOutputFormat(String value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, dpi, value);
  }
}
