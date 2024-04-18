Here's the proposed patch for the failing method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return new AnalysisEngineConfiguration.Builder()
            .setLanguages(globalConfig.getEnabledLanguages())
            .setClientProperty("clientPid", globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

In this patch, I've replaced the deprecated methods with their recommended alternatives. Specifically, I've replaced:

* `addEnabledLanguages` with `setLanguages`
* `setClientPid` with `setClientProperty("clientPid", ...)`

These changes should resolve the "cannot find symbol" error.