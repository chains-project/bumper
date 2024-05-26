Here is the updated code that should fix the error:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository repo = new org.sonarsource.sonarlint.core.languages.LanguagesImpl(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLiteEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .setEnabledLanguages(repo.getEnabledLanguagesInConnectedMode())
        .build();
}
```

In this updated code, I created a `LanguageSupportRepository` object called `repo` and initialized it with the list of enabled languages from `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()`. Then, I replaced the call to `addEnabledLanguages` with a call to `setEnabledLanguages` and passed it the list of enabled languages from `repo` (i.

I also removed the `--` marked changes from the code, and added the `++` marked changes.

I hope this helps! Let me know if you have any questions.