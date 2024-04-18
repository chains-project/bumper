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

This patch creates a new `Builder` object for the `AnalysisEngineConfiguration` class, and sets the necessary properties using the `set` methods. The `addEnabledLanguages` method has been replaced with the `setLanguages` method, which is a new method added in the updated version of the library. This should resolve the "cannot find symbol" error.