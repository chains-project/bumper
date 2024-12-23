Here's a proposed patch for the given client code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return new AnalysisEngineConfiguration.Builder()
            .setLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

This patch replaces the deprecated `addEnabledLanguages` method with the recommended `setLanguages` method. It also replaces the `AnalysisEngineConfiguration.builder()` method with the recommended `new AnalysisEngineConfiguration.Builder()` constructor.