Here is a proposed patch for the failing method:

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

This patch converts the set of enabled languages from `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` to a set of `org.sonarsource.sonarlint.core.commons.Language` objects, which is the type expected by the `addEnabledLanguages` method.

Note: This patch assumes that the `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()` method returns a `Set` of some type of `Language` object. If the actual return type of this method is different, the patch may need to be modified accordingly.