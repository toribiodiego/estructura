package com.estructura;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

public class DoclingOcrDemo {
  public static void main(String[] args) throws Exception {
    // Prefer system property; fall back to CLI arg
    final String input =
        System.getProperty("doc.input",
          (args.length > 0 ? args[0] : "")).trim();

    if (input.isEmpty()) {
      throw new IllegalArgumentException(
        "No input provided. Use -Ddoc.input=<url_or_path> or pass as first CLI arg.");
    }
    final String outDir = System.getProperty("doc.out", "out");

    System.out.println("Java → invoking CPython docling runner…");
    ProcessBuilder pb = new ProcessBuilder(
        "python3", "scripts/run_docling.py", input, outDir);
    pb.redirectErrorStream(true);
    Process p = pb.start();

    try (BufferedReader r =
           new BufferedReader(new InputStreamReader(p.getInputStream(), StandardCharsets.UTF_8))) {
      String output = r.lines().collect(Collectors.joining("\n"));
      int code = p.waitFor();
      if (code != 0) {
        System.err.println(output);
        throw new RuntimeException("Docling runner failed with exit code " + code);
      }
      System.out.println(output); // JSON with paths
    }
  }
}
