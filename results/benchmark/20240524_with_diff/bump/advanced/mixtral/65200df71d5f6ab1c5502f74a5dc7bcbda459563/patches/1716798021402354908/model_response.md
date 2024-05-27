Here's the patched method that should fix the error:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
        .build();
}
```

This patch creates a new variable `languageSupportRepository` to get the enabled languages from the `LanguageSupportRepository` instead of the `AnalysisEngineConfiguration`. It then uses the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages.