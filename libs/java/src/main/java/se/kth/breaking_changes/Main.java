package se.kth.breaking_changes;

import java.nio.file.Path;
import java.util.List;
import java.util.Set;

public class Main {

    static String client_id = "5fcd0c3ad7727850c47602b17530dc355e5bd097";
    static String project_folder = "pitest-mutation-testing-elements-plugin";
    static String old_version = "pitest-entry-1.9.11";
    static String new_version = "pitest-entry-1.10.0";
    public static void main(String[] args) {

        JApiCmpAnalyze jApiCmpAnalyze = new JApiCmpAnalyze(
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/breaking-good/clients/" + client_id + "/" + old_version + ".jar"),
            Path.of("/Users/federicobono/Documents/IT/UNI/thesis/code/breaking-good/clients/" + client_id + "/" + new_version + ".jar")
        );

        Set<ApiChange> apiChanges = jApiCmpAnalyze.getChanges();
        List<ApiChange> filteredList = apiChanges.stream()
            .filter(c -> c.getNotNullElement().contains("org.pitest.coverage"))
            .sorted((a, b) -> {
                return a.getNotNullElement().compareTo(b.getNotNullElement());
            })
            .toList();

        for (ApiChange apiChange : filteredList) {
            System.out.println(apiChange.toDiffString());
        }


    }
}
