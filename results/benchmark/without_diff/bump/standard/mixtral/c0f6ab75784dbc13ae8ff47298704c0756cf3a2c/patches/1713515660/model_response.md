Here's a proposed patch for the failing client code:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<String> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(lang -> lang.name()).collect(Collectors.toSet());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .withEnabledLanguages(enabledLanguages)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

In this patch, we first convert the set of `Language` objects returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to a set of strings containing the corresponding language names. Then, we use the `withEnabledLanguages` method of the `AnalysisEngineConfiguration.Builder` class to set the enabled languages. This method takes a set of strings as an argument, so it can be used with the set of language names that we created earlier.

Note that the `withEnabledLanguages` method is a new method added in a newer version of the SonarLint API. If the older `addEnabledLanguages` method is still required, it may be necessary to create a custom `AnalysisEngineConfiguration.Builder` implementation that provides this method. However, since the error message indicates that the `addEnabledLanguages` method cannot be found, it seems that this method is no longer available in the SonarLint API.