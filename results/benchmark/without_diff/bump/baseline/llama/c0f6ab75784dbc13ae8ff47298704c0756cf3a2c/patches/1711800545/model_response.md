```
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setDependencyVersion(DependencyVersion.of("org.sonar.api", "sonar-api-java", "1.10.0"))
                .build();
    }
```

In this proposal, we've added the `setDependencyVersion` method call to the `AnalysisEngineConfiguration.builder()` chain. This sets the version of the `org.sonar.api` dependency to `1.10.0`, which is the version that the `SonarLintEngine` class is compiled against.

This should fix the `Cannot find symbol` error, as the `setDependencyVersion` method is available in the `AnalysisEngineConfiguration.Builder` class, and the `DependencyVersion` class is available in the same package as the `AnalysisEngineConfiguration` class.