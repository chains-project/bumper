Here is the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setProperties(Stream.of(
            "sonar.sources", sorald.sonar.SonarLintEngine.globalConfig.getWorkDir(),
            "sonar.language", enabledLanguages.stream().map(Language::getName).collect(Collectors.joining(",")),
            "sonar.projectKey", sorald.sonar.SonarLintEngine.globalConfig.getClientPid(),
            "sonar.projectName", sorald.sonar.SonarLintEngine.globalConfig.getClientPid(),
            "sonar.sources", sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()
        ).collect(Collectors.toMap(Function.identity(), v -> Arrays.asList(v))))
        .build();
}
```

This patch uses the `setProperties` method instead of `addEnabledLanguages` to set the enabled languages. It also sets other required properties for the `AnalysisEngineConfiguration`. Note that this patch assumes that the `Language` class has a `getName` method that returns the name of the language as a string.