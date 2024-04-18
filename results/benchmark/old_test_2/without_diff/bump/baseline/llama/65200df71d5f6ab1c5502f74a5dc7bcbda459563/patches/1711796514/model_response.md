Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.fromMap(ImmutableMap.of("my-dependency", "1.2.3")))
            .build();
}
```
The patch adds the `setDependencyVersion` method to the `AnalysisEngineConfiguration.builder()` chain, which sets the version of the dependency to "1.2.3". This resolves the "cannot find symbol" error by providing a valid version for the dependency.