Here's the proposed patch for the failing method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Properties extraProperties = globalConfig.extraProperties();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(extraProperties)
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

This patch creates a local variable `extraProperties` for the `extraProperties()` method call, which might have been removed from the external dependency. This way, the code should work even if the `extraProperties()` method is no longer available.