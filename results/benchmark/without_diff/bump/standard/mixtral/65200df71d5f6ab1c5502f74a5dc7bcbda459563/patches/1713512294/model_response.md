Here's a fixed version of the method using the added library method `setEnabledLanguages`:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(language -> language.name()).collect(Collectors.toSet()))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This version converts the `Set<Language>` returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to a `Set<String>` containing the language names using Java 8 streams. The `addEnabledLanguages` method has been replaced with `setEnabledLanguages` which accepts a `Set<String>` instead of a `Set<Language>`.