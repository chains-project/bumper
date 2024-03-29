Here's a proposed patch to fix the error:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return new AnalysisEngineConfigurationBuilder()
            .withEnabledLanguages(globalConfig.getEnabledLanguages())
            .withClientPid(globalConfig.getClientPid())
            .withExtraProperties(globalConfig.extraProperties())
            .withWorkDir(globalConfig.getWorkDir())
            .withModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

Note: I made the assumption that `AnalysisEngineConfiguration.builder()` was replaced with `new AnalysisEngineConfigurationBuilder()` in the updated version of the external dependency. If this is not the case, the error may still persist.