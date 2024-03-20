Here's a patch for the given code failure:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Properties extraProperties = new Properties();
    extraProperties.putAll(globalConfig.extraProperties());

    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(extraProperties)
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```

The issue seems to be related to the `.setExtraProperties()` method not working as expected with the `globalConfig.extraProperties()` call. To fix this, we create a new `Properties` object, add all the properties from `globalConfig.extraProperties()` to this new object, and then pass it to the `.setExtraProperties()` method.