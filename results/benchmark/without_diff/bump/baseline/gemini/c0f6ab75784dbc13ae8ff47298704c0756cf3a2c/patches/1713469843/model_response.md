```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    // Initialize the builder with the global configuration
    AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(globalConfig.getEnabledLanguages())
        .setClientPid(globalConfig.getClientPid())
        .setWorkDir(globalConfig.getWorkDir())
        .setModulesProvider(globalConfig.getModulesProvider());

    // Extract the extra properties from the global configuration
    Map<String, Object> extraProperties = globalConfig.extraProperties();

    // Add the extra properties to the builder
    builder.setExtraProperties(extraProperties);

    // Return the built AnalysisEngineConfiguration
    return builder.build();
}
```