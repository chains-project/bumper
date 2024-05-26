Here is the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setProperties(Stream.of(
            "sonar.lang.patterns", String.join(",", enabledLanguages.stream().map(lang -> lang.name()).toArray(String[]::new)),
            "sonar.sources", ".",
            "sonar.tests", ""
        ).collect(Collectors.toMap(k -> k, v -> v)))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch converts the set of enabled languages to a comma-separated list of language names, which can be set as a property of the analysis engine configuration. This way, we avoid using the `addEnabledLanguages` method, which is not available in the version of the library that you are using. Instead, we set the `sonar.lang.patterns` property to indicate the enabled languages.