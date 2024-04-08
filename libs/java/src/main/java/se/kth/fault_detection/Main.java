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

    static String client_id = "24d4a90ec1b375751e71f33d18949405c9529d77";
    static String project_folder = "jcabi-s3";
    static String dependency_group_id = "";
    
    // static String dependency_group_id = "net.datafaker";

    public static void main(String[] args) {

        MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(new File("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + project_folder + "/" + client_id + ".log"));
        // MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(new File("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/1ef97ea6c5b6e34151fe6167001b69e003449f95/patched_code/1709041236/flink-faker/1ef97ea6c5b6e34151fe6167001b69e003449f95.log"));

        try {
            MavenErrorLog log = mavenLog.analyzeCompilationErrors();
            String project = "/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id;

            log.getErrorInfo().forEach((k, v) -> {
                System.out.println("Fault: " + k);
                FaultDetector detector = new FaultDetector(v);
                List<DetectedFault> results = detector.detectFaults(project + k);

                results.forEach(r -> {
                    System.out.println("ERROR #" + r.getIdentifier());
                    System.out.println("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + r.errorInfo.getClientFilePath());
                    System.out.println(r.errorInfo.getClientLinePosition());
                    System.out.println(r.clientLineNumber + ":" + r.clientEndLineNumber);
                });

                if(results.size() <= 0) {
                    System.out.println("WARNING: no error detected from this");
                }
            });


        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

}
