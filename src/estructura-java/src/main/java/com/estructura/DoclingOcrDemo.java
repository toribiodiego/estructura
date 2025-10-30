package com.estructura;

import com.estructura.docling.DoclingResult;
import com.estructura.docling.DoclingRunner;
import com.estructura.docling.DoclingRunnerException;

import java.nio.file.InvalidPathException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class DoclingOcrDemo {
  public static void main(String[] args) {
    final String input = System.getProperty("doc.input", (args.length > 0 ? args[0] : "")).trim();
    if (input.isEmpty()) {
      throw new IllegalArgumentException(
          "No input provided. Use -Ddoc.input=<url_or_path> or pass as first CLI arg.");
    }
    final String outDir = System.getProperty("doc.out", "out");

    Path outPath;
    try {
      outPath = Paths.get(outDir);
    } catch (InvalidPathException e) {
      throw new IllegalArgumentException("Invalid output directory: " + outDir, e);
    }

    DoclingRunner runner = new DoclingRunner();
    try {
      DoclingResult result = runner.ingest(input, outPath);
      System.out.printf("Docling document created (version=%s)%n", result.doclingVersion());
      if (result.snippet() != null && !result.snippet().isBlank()) {
        System.out.println("Snippet:");
        System.out.println(result.snippet());
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
}
