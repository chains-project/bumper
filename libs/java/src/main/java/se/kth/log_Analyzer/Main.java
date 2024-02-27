package se.kth.log_Analyzer;

import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        String path = "/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/1ef97ea6c5b6e34151fe6167001b69e003449f95/patched_code/1709041236/flink-faker/1ef97ea6c5b6e34151fe6167001b69e003449f95.log";
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
