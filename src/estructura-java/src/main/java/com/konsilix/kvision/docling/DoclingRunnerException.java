package com.konsilix.kvision.docling;

/**
 * Checked exception for wrapping Docling ingestion failures.
 */
public class DoclingRunnerException extends Exception {
  public DoclingRunnerException(String message) {
    super(message);
  }

  public DoclingRunnerException(String message, Throwable cause) {
    super(message, cause);
  }
}
