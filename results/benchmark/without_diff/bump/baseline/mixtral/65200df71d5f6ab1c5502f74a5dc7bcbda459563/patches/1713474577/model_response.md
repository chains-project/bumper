Here's the proposed patch:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    DependencyCheckConfiguration globalConfig = DependencyCheckConfiguration.getInstance();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

This patch creates a new variable `globalConfig` of type `DependencyCheckConfiguration` and assigns it the singleton instance of `DependencyCheckConfiguration`. This should resolve the "cannot find symbol" error.