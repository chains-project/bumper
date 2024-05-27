Here's a patch that you can apply to the code to fix the error:

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

The error message indicates that the `addEnabledLanguages` method is no longer available in the `AnalysisEngineConfiguration.Builder` class. Instead, you can use the `setEnabledLanguages` method to set the enabled languages.

Note that I've created a new variable `enabledLanguages` to hold the set of enabled languages, and then passed this variable to the `setEnabledLanguages` method. This makes the code easier to read and understand.