Here is a potential patch for the code:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<String> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(lang -> lang.name()).collect(Collectors.toSet());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(enabledLanguages)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch converts the set of `Language` objects returned by `getEnabledLanguages()` to a set of strings representing the language names. It then uses the `setEnabledLanguages()` method of the `AnalysisEngineConfiguration.Builder` to set the enabled languages.

Note that this patch assumes that the `Language` class has a `name()` method that returns a string representation of the language. If this is not the case, you may need to modify the lambda expression in the `map()` method to extract the language name in a different way.