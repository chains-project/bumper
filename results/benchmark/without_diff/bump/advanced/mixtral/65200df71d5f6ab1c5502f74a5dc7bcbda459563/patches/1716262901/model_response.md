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
The error is caused by the fact that the `addEnabledLanguages` method has been removed in a recent version of the `AnalysisEngineConfiguration.Builder` class. Instead, you can use the `setEnabledLanguages` method to set the enabled languages.

Additionally, I have created a local variable `enabledLanguages` to store the enabled languages, and then pass it to the `setEnabledLanguages` method. This makes the code easier to read and understand.

I hope this helps! Let me know if you have any questions.