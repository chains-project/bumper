package se.kth.breaking_changes;

import java.nio.file.Path;
import java.util.List;
import java.util.Set;

public class Main {

    static String client_id = "7f7de81d28b68b091bef2e6f6ffd1836167be6ea";
    // static String project_folder = "snmpman";
    static String old_version = "snmp4j-agent-3.0.3";
    static String new_version = "snmp4j-agent-3.6.6";
    static String org_id = "org.snmp4j";
    public static void main(String[] args) {
        JApiCmpAnalyze jApiCmpAnalyze = new JApiCmpAnalyze(
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + old_version + ".jar"),
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + new_version + ".jar")
        );

        Set<ApiChange> apiChanges = jApiCmpAnalyze.getChanges();
        List<ApiChange> filteredList = apiChanges.stream()
            .filter(c -> c.getValue().contains(org_id))
            .filter(c -> c.getValue().contains("ManagedObject"))
            .sorted((a, b) -> {
                return a.getValue().compareTo(b.getValue());
            })
            .toList();

        for (ApiChange apiChange : filteredList) {
            System.out.println(apiChange.toDiffString());
        }


    }
}
