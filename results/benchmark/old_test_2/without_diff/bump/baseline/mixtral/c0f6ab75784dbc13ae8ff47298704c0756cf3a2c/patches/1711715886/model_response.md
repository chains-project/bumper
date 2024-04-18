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

This patch creates a new `Builder` object for the `AnalysisEngineConfiguration` class, and sets the various properties using the `set` methods. The `addEnabledLanguages` method has been replaced with `setLanguages` to match the updated API of the `AnalysisEngineConfiguration.Builder` class. The `setClientPid` and `setExtraProperties` methods are unchanged, while the `setWorkDir` method has been renamed to `setWorkDir`. Finally, the `setModulesProvider` method has been left unchanged. This patch should resolve the "cannot find symbol" error.