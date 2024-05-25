Here is a proposed patch for the failing client code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Properties extraProperties = globalConfig.extraProperties();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(extraProperties)
            .setWorkDir(new File(extraProperties.getProperty("work.dir")))
            .setModulesProvider(new DefaultModulesProvider(extraProperties))
            .build();
}
```

This patch creates a new variable `extraProperties` to hold the extra properties from `globalConfig`. It then uses this variable to set the work directory and modules provider using the `File` and `DefaultModulesProvider` classes, respectively. These classes were added in a newer version of the external dependency and should be available for use.