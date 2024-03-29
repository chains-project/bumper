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
It appears that the issue is caused by the use of the `addEnabledLanguages` method, which has been removed in the new version of the library. Instead, we can use the `setLanguages` method, which has been added in the new version, to set the enabled languages. Additionally, the `AnalysisEngineConfiguration.builder()` method has been replaced with `new AnalysisEngineConfiguration.Builder()` in the new version.