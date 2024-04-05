Here's a proposed patch for the failing method:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<String> languageSet = new HashSet<>();
    for (org.sonarsource.sonarlint.core.commons.Language language : sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()) {
        languageSet.add(language.name());
    }
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(languageSet)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```
In this patch, I created a new `HashSet` called `languageSet` to store the enabled languages as strings. Then, I iterated over the `getEnabledLanguages()` method and added each language's name to the set. Finally, I replaced the `addEnabledLanguages()` method with `setEnabledLanguages()` and passed in the `languageSet`. This should resolve the "cannot find symbol" error.