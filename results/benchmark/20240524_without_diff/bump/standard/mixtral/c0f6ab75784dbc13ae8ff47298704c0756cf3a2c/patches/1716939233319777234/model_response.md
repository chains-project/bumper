Here's a fixed version of the method that uses the `AnalysisEngineConfiguration.Builder`'s `addEnabledLanguages(String...)` method instead of `addEnabledLanguages(Set<Language>)` method:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream()
            .map(Language::getName)
            .toArray(String[]::new)
        )
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```
This version converts the `Set<Language>` returned by `SonarLintEngine.globalConfig.getEnabledLanguages()` to an array of language names using the `Language.getName()` method and the `Stream` API. It then passes this array to the `addEnabledLanguages(String...)` method.