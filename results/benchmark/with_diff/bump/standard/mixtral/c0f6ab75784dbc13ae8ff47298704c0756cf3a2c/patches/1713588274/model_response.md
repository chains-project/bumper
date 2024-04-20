Here's the proposed patch to fix the error:

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

In the patched code, we get an instance of `LanguageSupportRepository` from `SonarLintEngine.globalConfig` and use its `getEnabledLanguagesInConnectedMode()` method to get the set of enabled languages. We then pass this set to the `setEnabledLanguages()` method of the `AnalysisEngineConfiguration.Builder` to set the enabled languages.

Note that the `getEnabledLanguages()` method has been removed in the new library version, and we cannot use it anymore. Instead, we use the new method `getEnabledLanguagesInConnectedMode()` to get the set of enabled languages in connected mode.