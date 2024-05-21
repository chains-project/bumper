Here's a proposed patch for the failing client code:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<String> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(language -> language.name()).collect(Collectors.toSet());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .withEnabledLanguages(enabledLanguages)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch converts the set of `Language` objects returned by `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to a set of strings representing the language names, and uses the `withEnabledLanguages()` method instead of `addEnabledLanguages()` to set the enabled languages. This should fix the "cannot find symbol" error caused by the removed `addEnabledLanguages()` method.