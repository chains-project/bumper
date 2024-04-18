Here is a proposed patch to fix the error:

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

I made the following changes:

* I replaced `AnalysisEngineConfiguration.builder()` with `new AnalysisEngineConfiguration.Builder()` to use the constructor instead of the static builder method.
* I replaced `addEnabledLanguages()` with `setLanguages()` to use the correct method for setting the enabled languages.
* I removed the `@Override` decorator since the method is not overriding any method in the new version.

I hope this helps! Let me know if you have any questions or if you need further assistance.