Here's the fixed version of the method using `++` added library methods:

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

In this solution, I replaced the `addEnabledLanguages` method with `setEnabledLanguages`, which accepts a `Set` of `org.sonarsource.sonarlint.core.commons.Language`. Since the original `Set` contains custom `Language` objects, I had to convert them to their corresponding `org.sonarsource.sonarlint.core.commons.Language` counterparts using the `valueOf` method.