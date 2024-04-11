Here is a possible patch for the `buildAnalysisEngineConfiguration()` method:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository repo = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(repo.getEnabledLanguagesInConnectedMode())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```
The main change is to replace the call to `addEnabledLanguages()` with a call to `setEnabledLanguages()`, and to use the new method `getEnabledLanguagesInConnectedMode()` from the `LanguageSupportRepository` class to get the set of enabled languages.

Note that I had to create a new instance of `LanguageSupportRepository` because it is not clear from the code snippet you provided how to get a reference to it. You may need to adjust this part of the code to fit your specific use case.