package se.kth.fault_detection;

import se.kth.log_Analyzer.MavenErrorLog;
import se.kth.log_Analyzer.MavenLogAnalyzer;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class Main {

    // static String client_id = "1ef97ea6c5b6e34151fe6167001b69e003449f95";
    // static String project_folder = "flink-faker";
    // static String dependency_group_id = "net.datafaker";

    static String client_id = "5fcd0c3ad7727850c47602b17530dc355e5bd097";
    static String project_folder = "pitest-mutation-testing-elements-plugin";
    static String dependency_group_id = "org.pitest";

    public static void main(String[] args) {

        MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(new File("/Users/federicobono/Documents/IT/UNI/thesis/code/breaking-good/clients/" + client_id + "/" + project_folder + "/" + client_id + ".log"));

        try {
            MavenErrorLog log = mavenLog.analyzeCompilationErrors();
            String project = "/Users/federicobono/Documents/IT/UNI/thesis/code/breaking-good/clients/" + client_id;

            log.getErrorInfo().forEach((k, v) -> {
                FaultDetector detector = new FaultDetector(dependency_group_id, v);
                List<DetectedFault> results = detector.detectFaults(project + k);

                results.forEach(System.out::println);
            });


        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

}
