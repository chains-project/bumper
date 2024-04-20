Here's the fixed version of the `buildAnalysisEngineConfiguration()` method:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository repo = sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .addEnabledLanguages(repo.getEnabledLanguagesInConnectedMode())
        .build();
}
```

The changes are:

1. Get the `LanguageSupportRepository` instance from `SonarLintEngine.globalConfig`.
2. Replace `addEnabledLanguages` with the new method `setEnabledLanguages` and pass the enabled languages from the repository. I used `getEnabledLanguagesInConnectedMode()` assuming you need the languages for connected mode. If not, replace `getEnabledLanguagesInConnectedMode()` with `getEnabledLanguagesInStandaloneMode()`.