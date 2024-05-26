Here's the proposed patch for the `buildAnalysisEngineConfiguration()` method:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream()
            .map(language -> org.sonarsource.sonarlint.core.commons.Language.valueOf(language.name()))
            .collect(Collectors.toSet()))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

The patch converts the `Set<sorald.sonar.SonarLintEngine.Language>` to `Set<org.sonarsource.sonarlint.core.commons.Language>` by using the `Stream` API and `valueOf()` method. This is needed because the `addEnabledLanguages()` method has been removed and replaced with `setEnabledLanguages()`. The new method accepts a `Set` of `org.sonarsource.sonarlint.core.commons.Language` instead of a `Set` of `sorald.sonar.SonarLintEngine.Language`.