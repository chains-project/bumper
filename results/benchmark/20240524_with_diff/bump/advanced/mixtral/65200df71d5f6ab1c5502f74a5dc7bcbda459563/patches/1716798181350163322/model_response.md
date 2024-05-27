Here's the fixed version of the method using the new library methods:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
        .build();
}
```

In this version, I replaced the `addEnabledLanguages` method with `setEnabledLanguages`. I also introduced the `LanguageSupportRepository` variable to get the enabled languages using the new method `getEnabledLanguagesInConnectedMode`.