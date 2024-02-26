package se.kth.log_Analyzer;

import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(new File("benchmarks/bump/clients/9836e07e553e29f16ee35b5d7e4d0370e1789ecd/docker-adapter/9836e07e553e29f16ee35b5d7e4d0370e1789ecd.log"));

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
