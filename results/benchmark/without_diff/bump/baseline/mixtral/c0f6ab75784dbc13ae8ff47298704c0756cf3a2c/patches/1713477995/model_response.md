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

This patch removes the use of the `addEnabledLanguages` method, which might have been removed in a newer library version. Instead, I've used the `setLanguages` method, which is likely the added alternative. This should resolve the "cannot find symbol" error.