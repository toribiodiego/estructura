package com.estructura.docling;

/**
 * Configuration for DoclingRunner.
 */
public record DoclingRunnerOptions(
    boolean runDocling,
    boolean runOcr,
    boolean progress,
    boolean useCache,
    boolean tableStructure,
    boolean verbose,
    Integer maxPages,
    Integer dpi
) {
  public static DoclingRunnerOptions defaults() {
    return new DoclingRunnerOptions(true, true, false, false, false, false, null, 120);
  }

  public DoclingRunnerOptions withRunDocling(boolean value) {
    return new DoclingRunnerOptions(value, runOcr, progress, useCache, tableStructure, verbose, maxPages, dpi);
  }

  public DoclingRunnerOptions withRunOcr(boolean value) {
    return new DoclingRunnerOptions(runDocling, value, progress, useCache, tableStructure, verbose, maxPages, dpi);
  }

  public DoclingRunnerOptions withProgress(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, value, useCache, tableStructure, verbose, maxPages, dpi);
  }

  public DoclingRunnerOptions withUseCache(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, value, tableStructure, verbose, maxPages, dpi);
  }

  public DoclingRunnerOptions withMaxPages(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, verbose, value, dpi);
  }

  public DoclingRunnerOptions withDpi(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, verbose, maxPages, value);
  }

  public DoclingRunnerOptions withTableStructure(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, value, verbose, maxPages, dpi);
  }

  public DoclingRunnerOptions withVerbose(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, value, maxPages, dpi);
  }
}
