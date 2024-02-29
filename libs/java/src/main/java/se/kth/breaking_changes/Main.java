package se.kth.breaking_changes;

import java.nio.file.Path;
import java.util.List;
import java.util.Set;

public class Main {

    static String client_id = "4a3efad6e00824e5814b9c8f571c9c98aad40281";
    // static String project_folder = "snmpman";
    static String old_version = "dss-pades-5.9";
    static String new_version = "dss-pades-5.10.2";
    static String org_id = "eu.europa.ec.joinup.sd-dss";
    public static void main(String[] args) {
        JApiCmpAnalyze jApiCmpAnalyze = new JApiCmpAnalyze(
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + old_version + ".jar"),
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + new_version + ".jar")
        );

        Set<ApiChange> apiChanges = jApiCmpAnalyze.getChanges();
        List<ApiChange> filteredList = apiChanges.stream()
            // .filter(c -> c.getValue().contains(org_id))
            // .filter(c -> c.getValue().contains("eu.europa.esig.dss.pades"))
            .filter(c -> c.getValue().contains("CertificationPermission"))
            .sorted((a, b) -> {
                return a.getValue().compareTo(b.getValue());
            })
            .toList();

        for (ApiChange apiChange : filteredList) {
            System.out.println(apiChange.toDiffString());
        }


    }
}
