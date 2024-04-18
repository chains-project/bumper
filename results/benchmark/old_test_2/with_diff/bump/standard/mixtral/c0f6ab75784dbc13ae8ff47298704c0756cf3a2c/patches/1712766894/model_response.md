Here is a possible patch for the `buildAnalysisEngineConfiguration()` method:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository repo = sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .setEnabledLanguages(repo.getEnabledLanguagesInConnectedMode())
        .build();
}
```

This patch uses the new `getEnabledLanguagesInConnectedMode()` method of the `LanguageSupportRepository` class to get the enabled languages. It also removes the call to `addEnabledLanguages()`, which is no longer available in the new version of the library.

Note that this patch assumes that the `LanguageSupportRepository` instance returned by `sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository()` is not `null`. If this is not the case, you may need to add a null check before calling the `getEnabledLanguagesInConnectedMode()` method.