Here's a possible patch for the given code snippet:

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

In this patch, I have replaced the use of the static `builder()` method with the constructor `new AnalysisEngineConfiguration.Builder()`. Additionally, I have replaced the deprecated `addEnabledLanguages()` method with the `setLanguages()` method. These changes should resolve the "cannot find symbol" error.