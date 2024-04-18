Here's a proposed patch for the failing client code:

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

Note that I changed the method `addEnabledLanguages` to `setLanguages` as the former is not present in the new version of the library. Additionally, I replaced `AnalysisEngineConfiguration.builder()` with `new AnalysisEngineConfiguration.Builder()` since the former is no longer available.