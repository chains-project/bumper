Here's a proposed patch for the given failing method. This patch replaces the usage of `addEnabledLanguages` method with the equivalent `withEnabledLanguages` method, which was added in a later version of the library.

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .withEnabledLanguages(new java.util.HashSet<>(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

This patch should resolve the compilation error by using the `withEnabledLanguages` method instead of the removed `addEnabledLanguages` method.