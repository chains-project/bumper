Here is a proposed patch for the failing client code:

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

This patch creates a new `AnalysisEngineConfiguration.Builder` object and sets the necessary properties using the `set` methods. Note that the `addEnabledLanguages` method has been changed to `setLanguages` to reflect the method in the updated library. This should resolve the "cannot find symbol" error.