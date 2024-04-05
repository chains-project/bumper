Here is a potential patch for the failing method:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setProperties(ImmutableMap.of("sonarlint.langs", String.join(",", enabledLanguages.stream().map(Language::getName).collect(Collectors.toList()))))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch removes the call to `addEnabledLanguages` and instead sets a property on the configuration that specifies the enabled languages as a comma-separated list of language names. This uses the `ImmutableMap` and `Stream` classes from the Guava library, which have been added in a recent version of the external dependency.

Note that this patch assumes that the `Language` class has a `getName` method that returns the name of the language as a string. If this is not the case, you may need to modify the lambda expression in the `map` method to extract the language name in a different way.