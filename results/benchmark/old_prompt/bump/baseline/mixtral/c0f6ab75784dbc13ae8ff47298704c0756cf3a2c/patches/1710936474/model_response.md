Here's a patch to fix the error in the `buildAnalysisEngineConfiguration()` method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return new AnalysisEngineConfiguration.Builder()
            .setEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

The original code used a static import for `AnalysisEngineConfiguration.builder()`, which might not be available anymore due to the updated dependency. I changed the code to use the constructor `new AnalysisEngineConfiguration.Builder()` instead, which should be more reliable. The rest of the code remains the same.