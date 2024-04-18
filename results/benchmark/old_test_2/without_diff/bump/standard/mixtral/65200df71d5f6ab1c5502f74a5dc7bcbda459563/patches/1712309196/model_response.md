Here's a proposed patch that should fix the error:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setOptions(enabledLanguages.stream()
            .collect(java.util.stream.Collectors.toMap(
                input -> input.name(),
                input -> "true")))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch converts the set of enabled languages to a map of language names to boolean values, which can be passed to the `setOptions` method of the `AnalysisEngineConfiguration.Builder`. This method was added in version 6.7 of the SonarLint API, so if you are using an earlier version, this patch will not work.