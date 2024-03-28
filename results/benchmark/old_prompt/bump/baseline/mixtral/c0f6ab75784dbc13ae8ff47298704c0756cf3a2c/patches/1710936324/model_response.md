Here's a patch for the failing method. It seems like `AnalysisEngineConfiguration.builder()` might be causing the issue, so we can try using `new AnalysisEngineConfiguration()` instead. We will also need to update the method of setting properties accordingly:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    AnalysisEngineConfiguration config = new AnalysisEngineConfiguration();
    config.addEnabledLanguages(globalConfig.getEnabledLanguages())
        .setClientPid(globalConfig.getClientPid())
        .setExtraProperties(globalConfig.extraProperties())
        .setWorkDir(globalConfig.getWorkDir())
        .setModulesProvider(globalConfig.getModulesProvider());
    return config;
}
```

This code initializes a new `AnalysisEngineConfiguration` object and sets its properties using the fluent builder-like method chain. This should resolve the compilation error.