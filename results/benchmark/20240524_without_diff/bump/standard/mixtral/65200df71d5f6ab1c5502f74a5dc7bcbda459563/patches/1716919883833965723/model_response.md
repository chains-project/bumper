Here's a fixed version of the method that should resolve the error:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream()
            .map(language -> (org.sonarsource.sonarlint.core.commons.Language) language)
            .collect(Collectors.toSet()))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

The error is caused by the fact that the `addEnabledLanguages` method has been removed from the `AnalysisEngineConfiguration.Builder` class. Instead, we can use the `setEnabledLanguages` method to set the enabled languages.

The `getEnabledLanguages` method of `SonarLintEngine.globalConfig` returns a `Set<sorald.sonar.SonarLintEngine.Language>`, but the `setEnabledLanguages` method expects a `Set<org.sonarsource.sonarlint.core.commons.Language>`. To convert the set, we can use the `stream` method to create a stream of the elements, map each element to its corresponding `org.sonarsource.sonarlint.core.commons.Language` equivalent using a lambda expression, and then collect the elements back into a set using the `collect` method.

Note that this solution assumes that there is a way to convert each `sorald.sonar.SonarLintEngine.Language` to its corresponding `org.sonarsource.sonarlint.core.commons.Language` equivalent. If this is not the case, then additional changes may be necessary.