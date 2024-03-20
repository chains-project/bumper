Here is a patch for the failing client code:
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
The issue is caused by the use of a `builder()` method, which has been removed from the library. Instead, we can use the `new` keyword to create a new instance of the `AnalysisEngineConfiguration.Builder` class. The rest of the code remains unchanged.