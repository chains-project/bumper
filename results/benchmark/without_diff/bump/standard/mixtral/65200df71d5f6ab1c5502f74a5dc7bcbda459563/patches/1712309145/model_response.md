Here's a proposed patch to fix the error:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<String> languageKeys = new HashSet<>(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(languageKeys)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

In this patch, we convert the set of `Language` objects returned by `getEnabledLanguages` to a set of strings representing the language keys. This is because the `addEnabledLanguages` method now expects a set of strings instead of a set of `Language` objects.

Note that this patch assumes that the `Language` class has a `toString` method that returns the language key as a string. If this is not the case, you may need to modify the code to extract the language key from the `Language` object in a different way.