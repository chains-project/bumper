Here's a patch for the failing method. It seems that the `AnalysisEngineConfiguration.builder()` method is causing the issue, possibly due to a removed or renamed method in the library. To fix this, we can use the `AnalysisEngineConfiguration.createDefault()` method, which is a new method added in the library, to create a default configuration and then set the necessary properties.
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    AnalysisEngineConfiguration configuration = AnalysisEngineConfiguration.createDefault();
    return configuration
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```
This code creates a default `AnalysisEngineConfiguration` object using the `createDefault()` method, and then sets the necessary properties using the `addEnabledLanguages()`, `setClientPid()`, `setExtraProperties()`, `setWorkDir()`, and `setModulesProvider()` methods. Finally, the configuration is built using the `build()` method.