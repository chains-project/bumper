Here's a possible patch for the failing client code:

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

In this patch, we first convert the set of `Language` objects returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to a set of strings containing their names. This is because the `AnalysisEngineConfiguration.Builder` class does not have an `addEnabledLanguages` method, but it does have a `setEnabledLanguages` method that takes a set of strings.

Note that this patch assumes that the `Language` class has a `name` method that returns a string representation of the language. If this is not the case, you may need to modify the patch accordingly.