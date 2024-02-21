package se.kth.breaking_changes;

import java.nio.file.Path;
import java.util.List;
import java.util.Set;

public class Main {

    static String client_id = "0a11c04038eae517540051dbf51f7f26b7221f20";
    static String project_folder = "simplelocalize-cli";
    static String old_version = "snakeyaml-1.24";
    static String new_version = "snakeyaml-2.0";
    static String org_id = "org.yaml";
    public static void main(String[] args) {

        JApiCmpAnalyze jApiCmpAnalyze = new JApiCmpAnalyze(
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + old_version + ".jar"),
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/" + client_id + "/" + new_version + ".jar")
        );

        Set<ApiChange> apiChanges = jApiCmpAnalyze.getChanges();
        List<ApiChange> filteredList = apiChanges.stream()
            .filter(c -> c.getValue().contains(org_id))
            .filter(c -> c.getValue().contains("Constructor"))
            .sorted((a, b) -> {
                return a.getValue().compareTo(b.getValue());
            })
            .toList();

        for (ApiChange apiChange : filteredList) {
            System.out.println(apiChange.toDiffString());
        }


    }
}
