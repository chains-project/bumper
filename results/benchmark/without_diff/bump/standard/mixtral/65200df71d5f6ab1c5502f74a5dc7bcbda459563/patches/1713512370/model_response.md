Here's the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(enabledLanguages)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

In the original code, the `addEnabledLanguages` method is called with a `Set` of `Language` objects directly. However, it seems that the external dependency has been updated and the method now requires the `Set` to be passed as a variable instead. To fix the issue, I created a separate variable `enabledLanguages` to store the result of `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()`, and passed it as an argument to the `addEnabledLanguages` method.