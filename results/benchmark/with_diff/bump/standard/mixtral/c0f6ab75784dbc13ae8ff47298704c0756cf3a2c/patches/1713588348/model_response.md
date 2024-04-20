Here's the updated code that should fix the error:

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

In this updated code, I created a new variable `languageSupportRepository` of type `org.sonarsource.sonarlint.core.languages.LanguageSupportRepository` and used the method `getEnabledLanguagesInConnectedMode()` to get the enabled languages. This method was added in the new library version.

Note that the method `getEnabledLanguages()` was removed in the new library version, so I replaced it with the new method `getEnabledLanguagesInConnectedMode()`. Also, since the method `addEnabledLanguages()` is no longer available, I used the method `setEnabledLanguages()` instead.