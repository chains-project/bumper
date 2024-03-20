Here's a patch to fix the failing client code:
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
The issue here is that the `extraProperties()` method returns a `Map<String, String>` and the `setExtraProperties()` method of `AnalysisEngineConfiguration.Builder` expects a `Properties` object. In order to fix the issue, we create a new `Properties` object, put all the key-value pairs from `globalConfig.extraProperties()` into the `Properties` object, and then pass it to `setExtraProperties()`.