Here is a patch that you can apply to the code in order to fix the error:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Properties extraProperties = globalConfig.extraProperties();
    ModuleProvider modulesProvider = globalConfig.getModulesProvider();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(extraProperties)
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(modulesProvider)
            .build();
}
```

This patch creates local variables for the `extraProperties` and `modulesProvider` fields of the `globalConfig` object, and then passes these variables to the `AnalysisEngineConfiguration.builder()` method. This should fix the "cannot find symbol" error.

Note that I made a few assumptions about the `globalConfig` object and the `AnalysisEngineConfiguration.builder()` method, as I do not have access to the full codebase. If these assumptions are incorrect, you may need to modify the patch accordingly.