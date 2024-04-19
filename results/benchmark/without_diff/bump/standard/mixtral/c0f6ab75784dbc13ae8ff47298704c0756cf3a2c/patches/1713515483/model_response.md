Here's the proposed patch to fix the error:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(enabledLanguages)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

The patch creates a new variable `enabledLanguages` to store the enabled languages returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()`. Then, it uses the `setEnabledLanguages()` method instead of `addEnabledLanguages()` to set the enabled languages for the analysis engine configuration. This should fix the "cannot find symbol" error for the `addEnabledLanguages()` method.