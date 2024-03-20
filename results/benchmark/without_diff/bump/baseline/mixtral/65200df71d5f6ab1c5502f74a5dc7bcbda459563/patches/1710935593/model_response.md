Here is a patch for the failing method that should fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Map<String, Object> extraProperties = globalConfig.extraProperties();
    String workDir = globalConfig.getWorkDir();
    Supplier<List<Module>> modulesProvider = globalConfig.getModulesProvider();

    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .putAllExtraProperties(extraProperties)
            .setWorkDir(workDir)
            .setModulesProvider(modulesProvider)
            .build();
}
```
The issue is that the `setExtraProperties` method was removed and replaced with `putAllExtraProperties` in the new version. Additionally, the `setWorkDir` method was changed to take a simple string instead of a `WorkDir` object. The `getModulesProvider` method was also changed to return a `Supplier<List<Module>>` instead of a `ModulesProvider` object. These changes are reflected in the updated code.