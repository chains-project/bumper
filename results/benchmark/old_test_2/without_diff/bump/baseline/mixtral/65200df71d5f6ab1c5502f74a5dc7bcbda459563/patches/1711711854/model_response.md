Here's a proposed patch to fix the error:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    FileWorkingDirProvider workDirProvider = new FileWorkingDirProvider();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDirProvider(workDirProvider)
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

In this patch, we create a new `FileWorkingDirProvider` object and set it as the `WorkDirProvider` for the `AnalysisEngineConfiguration`. This should resolve the "cannot find symbol" error.