Here's a fixed version of the method using the added library method `addEnabledLanguages(java.util.Collection<java.lang.String>)`:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(lang -> lang.getName()).collect(Collectors.toList()))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This version converts the `Set<org.sonarsource.sonarlint.core.commons.Language>` returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to a `List<String>` by calling `getName()` on each element and streaming it to a list. The `addEnabledLanguages(java.util.Collection<java.lang.String>)` method is then used to add the list of language names to the `AnalysisEngineConfiguration.Builder`.