Here is a patch that can fix the error:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepositoryImpl();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
        .build();
}
```

This patch creates a new `LanguageSupportRepository` object and uses the new `getEnabledLanguagesInConnectedMode()` method to get the enabled languages. This should fix the "cannot find symbol" error.

Note that this patch assumes that the analysis engine is being run in connected mode. If it is being run in standalone mode, you should use the `getEnabledLanguagesInStandaloneMode()` method instead.

I hope this helps! Let me know if you have any questions.