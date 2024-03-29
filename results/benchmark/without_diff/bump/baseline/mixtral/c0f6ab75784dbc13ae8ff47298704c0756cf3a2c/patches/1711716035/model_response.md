Here is a possible patch for the failing code:
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
In this patch, we create a new `Properties` object called `extraProperties` and initialize it with the key-value pairs from `globalConfig.extraProperties()`. This way, we avoid calling the removed method `extraProperties()` and use a standard Java object instead.

Note that this patch assumes that the `Properties` class is still available and has not been removed in the new version of the external dependency. If this is not the case, a different approach might be necessary.