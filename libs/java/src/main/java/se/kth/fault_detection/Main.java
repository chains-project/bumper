package se.kth.fault_detection;

import se.kth.log_Analyzer.MavenErrorLog;
import se.kth.log_Analyzer.MavenLogAnalyzer;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class Main {

    // static String client_id = "9836e07e553e29f16ee35b5d7e4d0370e1789ecd";
    // static String project_folder = "docker-adapter";
    // static String dependency_group_id = "com.artipie";

    // static String client_id = "5fcd0c3ad7727850c47602b17530dc355e5bd097";
    // static String project_folder = "pitest-mutation-testing-elements-plugin";
    // static String dependency_group_id = "org.pitest";
    
    static String dependency_group_id = "net.datafaker";

    public static void main(String[] args) {

        // MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(new File("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + project_folder + "/" + client_id + ".log"));
        MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(new File("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/1ef97ea6c5b6e34151fe6167001b69e003449f95/patched_code/1709041236/flink-faker/1ef97ea6c5b6e34151fe6167001b69e003449f95.log"));

        try {
            MavenErrorLog log = mavenLog.analyzeCompilationErrors();
            String project = "/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/1ef97ea6c5b6e34151fe6167001b69e003449f95/patched_code/1709041236";

            log.getErrorInfo().forEach((k, v) -> {
                System.out.println("Fault: " + k);
                FaultDetector detector = new FaultDetector(dependency_group_id, v);
                List<DetectedFault> results = detector.detectFaults(project + k);

                results.forEach(r -> {
                    System.out.println("ERROR #" + r.getIdentifier());
                    System.out.println(r.errorInfo.getClientFilePath());
                    System.out.println(r.errorInfo.getClientLinePosition());
                    System.out.println(r.clientLineNumber + ":" + r.clientEndLineNumber);
                });
            });


        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

}
