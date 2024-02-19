package se.kth;


import picocli.CommandLine;
import se.kth.breaking_changes.ApiChange;
import se.kth.breaking_changes.JApiCmpAnalyze;
import se.kth.failure.Failure;
import se.kth.fault_detection.DetectedFault;
import se.kth.fault_detection.FaultDetector;
import se.kth.log_Analyzer.MavenErrorLog;
import se.kth.log_Analyzer.MavenLogAnalyzer;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;

public class Main {
    public static void main(String[] args) {
        int exitCode = new CommandLine(new Explaining()).execute(args);
        System.exit(exitCode);
    }

    @CommandLine.Command(name = "explaining", mixinStandardHelpOptions = true, version = "0.1")
    private static class Explaining implements Runnable {

        @CommandLine.Option(
                names = {"-c", "--client"},
                paramLabel = "Client project",
                description = "A client project to analyze.",
                required = true
        )
        Path client;

        @CommandLine.Option(
                names = {"-o", "--old-dependency"},
                paramLabel = "Old dependency",
                description = "The old dependency to analyze.",
                required = true
        )
        Path oldDependency;

        @CommandLine.Option(
                names = {"-n", "--new-dependency"},
                paramLabel = "New dependency",
                description = "The new dependency to analyze.",
                required = true
        )
        Path newDependency;

        @CommandLine.Option(
                names = {"-l", "--log"},
                paramLabel = "Maven log",
                description = "The maven log to analyze.",
                required = false
        )
        File mavenLog;

        @CommandLine.Option(
                names = {"-g", "--group-id"},
                paramLabel = "Dependency group ID",
                description = "The group ID of the dependency to analyze.",
                required = false
        )
        String dependencyGroupID;

        @Override
        public void run() {
            List<Failure> failures = new ArrayList<Failure>();

            JApiCmpAnalyze jApiCmpAnalyze = new JApiCmpAnalyze(oldDependency, newDependency);
            Set<ApiChange> apiChanges = jApiCmpAnalyze.getChanges();

            MavenLogAnalyzer mavenLog = new MavenLogAnalyzer(this.mavenLog);
            try {
                MavenErrorLog log = mavenLog.analyzeCompilationErrors();
                String project = this.client.toString();

                log.getErrorInfo().forEach((k, v) -> {
                    FaultDetector detector = new FaultDetector("org.pitest", v);
                    List<DetectedFault> results = detector.detectFaults(project + k);

                    results.forEach(fault -> {
                        failures.add(new Failure(
                            apiChanges,
                            fault
                        ));
                    });
                });

                ObjectWriter ow = new ObjectMapper().writer().withDefaultPrettyPrinter();
                System.out.println(ow.writeValueAsString(failures));
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }


}