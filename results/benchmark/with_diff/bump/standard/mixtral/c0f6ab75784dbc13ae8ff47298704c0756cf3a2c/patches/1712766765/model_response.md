Here's the fixed version of the `buildAnalysisEngineConfiguration()` method that uses the new method to get the enabled languages:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This version gets the `LanguageSupportRepository` from the `SonarLintEngine.globalConfig` object and uses the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages. The rest of the method remains unchanged.