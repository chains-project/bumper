Here's a fixed version of the method that uses the `AnalysisEngineConfiguration.Builder`'s `addEnabledLanguages(String...)` method instead:
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
This version converts the `Set<Language>` returned by `SonarLintEngine.globalConfig.getEnabledLanguages()` to an array of strings using the `toArray` method, and then passes that array to `addEnabledLanguages`. This should allow the code to compile and run successfully.