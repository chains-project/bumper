Here is a potential patch that you can apply to the code:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setEnabledLanguages(enabledLanguages)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```
This patch creates a new variable `enabledLanguages` to hold the set of enabled languages, and then uses the `setEnabledLanguages` method to set the languages on the `AnalysisEngineConfiguration.Builder`. This should fix the error caused by the missing `addEnabledLanguages` method.

Note that this patch assumes that the `getEnabledLanguages` method returns a `Set` of `Language` objects. If the return type is different, you may need to adjust the type of the `enabledLanguages` variable accordingly.