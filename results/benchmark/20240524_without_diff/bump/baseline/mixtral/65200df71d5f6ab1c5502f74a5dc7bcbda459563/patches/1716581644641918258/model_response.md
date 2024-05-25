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

This patch creates a local variable `extraProperties` for the `extraProperties()` method call, so that the method call only occurs once. This change should not affect the functionality of the code, but may help to resolve the "cannot find symbol" error.