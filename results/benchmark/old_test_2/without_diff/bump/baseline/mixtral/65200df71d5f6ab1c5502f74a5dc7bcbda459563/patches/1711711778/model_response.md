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

This patch creates a new `FileWorkingDirProvider` instance for the `setWorkDirProvider` method, which should resolve the "cannot find symbol" error. Note that this assumes that `FileWorkingDirProvider` is a new class that was added to replace the old `WorkDirProvider` interface. If this is not the case, you may need to modify the code accordingly.