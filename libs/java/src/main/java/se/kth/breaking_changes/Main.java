package se.kth.breaking_changes;

import java.nio.file.Path;
import java.util.List;
import java.util.Set;

public class Main {

    static String client_id = "0abf7148300f40a1da0538ab060552bca4a2f1d8";
    static String project_folder = "xdev-software";
    static String old_version = "jasperreports-6.18.1";
    static String new_version = "jasperreports-6.19.1";
    static String org_id = "net.sf.jasperreports";
    public static void main(String[] args) {
        JApiCmpAnalyze jApiCmpAnalyze = new JApiCmpAnalyze(
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + old_version + ".jar"),
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + new_version + ".jar")
        );

        Set<ApiChange> apiChanges = jApiCmpAnalyze.getChanges();
        List<ApiChange> filteredList = apiChanges.stream()
            .filter(c -> c.getValue().contains(org_id))
            .sorted((a, b) -> {
                return a.getValue().compareTo(b.getValue());
            })
            .toList();

        for (ApiChange apiChange : filteredList) {
            System.out.println(apiChange.toDiffString());
        }


    }
}
