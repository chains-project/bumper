Here's a possible patch for the code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    DependencyCheckingAnalysisEngineConfiguration.Builder builder = DependencyCheckingAnalysisEngineConfiguration.builder();
    builder.setClientPid(globalConfig.getClientPid());
    builder.setExtraProperties(globalConfig.extraProperties());
    builder.setWorkDir(globalConfig.getWorkDir());
    builder.setModulesProvider(globalConfig.getModulesProvider());
    globalConfig.getEnabledLanguages().forEach(builder::addEnabledLanguage);
    return builder.build();
}
```

In this patch, I've used the `DependencyCheckingAnalysisEngineConfiguration` class instead of `AnalysisEngineConfiguration`, which seems to be a more appropriate class for the task at hand. I've also used the `addEnabledLanguage` method instead of `addEnabledLanguages` to add enabled languages one by one. This should fix the "cannot find symbol" error.