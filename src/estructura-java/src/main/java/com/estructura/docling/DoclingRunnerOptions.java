/* (C) 2026 Diego Toribio. All rights reserved. */
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
    boolean imageAnnotations,
    boolean imageCapture,
    boolean verbose,
    Integer maxPages,
    Integer maxImagePages,
    Integer maxImagesPerPage,
    Integer maxTotalImages,
    Integer dpi,
    String outputFormat
) {
  public static DoclingRunnerOptions defaults() {
    return new DoclingRunnerOptions(true, true, false, false, false, false, false, false, null, 50, 20, 200, 120, "markdown");
  }

  public DoclingRunnerOptions withRunDocling(boolean value) {
    return new DoclingRunnerOptions(value, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withRunOcr(boolean value) {
    return new DoclingRunnerOptions(runDocling, value, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withProgress(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, value, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withUseCache(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, value, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withMaxPages(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, value, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withDpi(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, value, outputFormat);
  }

  public DoclingRunnerOptions withTableStructure(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, value, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withImageAnnotations(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, value, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withImageCapture(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, value, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withVerbose(boolean value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, value, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withOutputFormat(String value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, maxTotalImages, dpi, value);
  }

  public DoclingRunnerOptions withMaxImagePages(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, value, maxImagesPerPage, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withMaxImagesPerPage(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, value, maxTotalImages, dpi, outputFormat);
  }

  public DoclingRunnerOptions withMaxTotalImages(Integer value) {
    return new DoclingRunnerOptions(runDocling, runOcr, progress, useCache, tableStructure, imageAnnotations, imageCapture, verbose, maxPages, maxImagePages, maxImagesPerPage, value, dpi, outputFormat);
  }
}
