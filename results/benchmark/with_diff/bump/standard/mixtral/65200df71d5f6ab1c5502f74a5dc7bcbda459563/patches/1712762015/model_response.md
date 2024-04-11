Here is the proposed patch:

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

I created a new variable `languageSupportRepository` to store the `LanguageSupportRepository` instance, which allows us to use the new `getEnabledLanguagesInConnectedMode()` method.