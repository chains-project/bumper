Here's a fixed version of the method using `++` added library methods:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .withEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(lang -> (org.sonarsource.sonarlint.core.commons.Language) lang).collect(Collectors.toSet()))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch converts the `Set<sorald.sonar.SonarLintEngine.Language>` returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to a `Set<org.sonarsource.sonarlint.core.commons.Language>` using the Java Stream API. The `withEnabledLanguages` method is assumed to be an added method in the `Builder` class that accepts a `Set<org.sonarsource.sonarlint.core.commons.Language>`.