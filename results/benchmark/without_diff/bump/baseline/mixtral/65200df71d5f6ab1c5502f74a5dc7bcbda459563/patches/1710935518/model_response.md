Based on the information you've provided, it seems the primary issue here is a missing symbol (AnalysisEngineConfiguration) which is likely caused by an outdated or incorrect dependency. However, since you've mentioned that the solution should only involve changes to the client code, here's a modified version of the `buildAnalysisEngineConfiguration` method that wraps the `AnalysisEngineConfiguration.builder()` within a try-catch block to handle the missing symbol:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    AnalysisEngineConfiguration.Builder builder = null;
    try {
        builder = AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
    } catch (Exception e) {
        // Handle the missing symbol here, you can add a logging mechanism or create a default configuration
        // For the sake of simplicity, I'm creating a default configuration here
        builder = AnalysisEngineConfiguration.builder();
    }
    return builder.build();
}
```

This code attempts to create the `AnalysisEngineConfiguration` as before, but when it encounters the missing symbol, it falls back to creating a default configuration. You can replace the default configuration creation with a logging mechanism or any other appropriate error handling strategy based on your requirements.