Here is the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .addEnabledLanguages(enabledLanguages)
        .build();
}
```

In this patch, I created a new variable `enabledLanguages` to store the result of `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()`. Then, I used the `addEnabledLanguages` method by passing the `enabledLanguages` variable instead of calling the method directly on the `builder` object. This should fix the "cannot find symbol" error.