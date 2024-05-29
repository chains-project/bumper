Here's the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .addEnabledLanguages(enabledLanguages)
        .build();
}
```

In this patch, I created a new variable `enabledLanguages` to store the result of `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` and added it to the `AnalysisEngineConfiguration.Builder` using the `addEnabledLanguages` method. This should fix the "cannot find symbol" error caused by the missing method.