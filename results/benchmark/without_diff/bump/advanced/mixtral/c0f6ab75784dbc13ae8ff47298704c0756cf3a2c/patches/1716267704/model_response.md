Here is a patch that should fix the error:
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
The `addEnabledLanguages` method is no longer available in the `AnalysisEngineConfiguration.Builder` class. Instead, you can use the `setEnabledLanguages` method to set the enabled languages. I have created a new variable `enabledLanguages` to store the set of enabled languages returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()`. This variable is then passed to the `setEnabledLanguages` method.