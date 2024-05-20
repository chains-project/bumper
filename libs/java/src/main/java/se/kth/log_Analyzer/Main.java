package se.kth.log_Analyzer;

import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        String path = "/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/old_clients/38c9915f0cfdf0c1a2b17c3c6f283c23a0aac0cf/patched_code/test/java-api/38c9915f0cfdf0c1a2b17c3c6f283c23a0aac0cf.log";
        MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(new File(path));

        try {
            MavenErrorLog errorLog = mavenLog.analyzeCompilationErrors();
            errorLog.getErrorInfo().forEach((k, v) -> {
                v.forEach((e) -> {
                    System.out.println(e.errorMessage);
                    System.out.println(">>> " + e.additionalInfo + "\n");
                });
            });
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
}
