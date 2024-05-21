Here's the patched method using the new library methods:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository repo = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setEnabledLanguages(repo.getEnabledLanguagesInConnectedMode())
        .build();
}
```

This code creates a new `LanguageSupportRepository` object and uses the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages. I have assumed that the engine is running in connected mode. If not, replace `getEnabledLanguagesInConnectedMode()` with `getEnabledLanguagesInStandaloneMode()`.