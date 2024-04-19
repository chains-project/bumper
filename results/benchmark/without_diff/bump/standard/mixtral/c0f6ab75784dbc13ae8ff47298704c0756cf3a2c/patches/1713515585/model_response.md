Here's a fixed version of the code that uses the `AnalysisEngineConfiguration.builder()` method to create a new `Builder` instance, and then calls the `addEnabledLanguages(String...)` method to add the enabled languages:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().toArray(new String[0]))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

Note that I had to convert the `Set<String>` returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to an array of strings using the `toArray()` method. This is because the `addEnabledLanguages(String...)` method expects a variable number of `String` arguments, not a `Set<String>`.