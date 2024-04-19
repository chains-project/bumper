Here's a fixed version of the method that uses the added `addEnabledLanguages(java.util.Collection<? extends java.lang.String>)` method:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(lang -> lang.name()).collect(Collectors.toList()))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This version converts the `Set<sorald.sonar.SonarLintEngine.Language>` returned by `getEnabledLanguages()` to a `List<String>` by using the `name()` method on each `Language` object and then streaming the result to a list. The `addEnabledLanguages(java.util.Collection<? extends java.lang.String>)` method can then be used to add the enabled languages to the `AnalysisEngineConfiguration.Builder`.