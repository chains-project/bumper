Here's the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setOption(new org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Builder.Option<Set<org.sonarsource.sonarlint.core.commons.Language>>("sonar.lang.patterns", enabledLanguages))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

In this patch, we use the `setOption` method to add the enabled languages to the configuration. The `setOption` method allows us to add custom options to the configuration, which can be used by the analysis engine. We create a new `Option` object with the key `sonar.lang.patterns` and the value of the enabled languages. This will have the same effect as the `addEnabledLanguages` method.