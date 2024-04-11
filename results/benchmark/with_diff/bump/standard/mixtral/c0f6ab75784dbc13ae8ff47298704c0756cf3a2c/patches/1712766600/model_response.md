Here is a patch that you can apply to the failing method:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch creates a new `LanguageSupportRepository` object and uses the new `getEnabledLanguagesInConnectedMode()` method to get the enabled languages for the analysis engine configuration. The rest of the method remains unchanged.