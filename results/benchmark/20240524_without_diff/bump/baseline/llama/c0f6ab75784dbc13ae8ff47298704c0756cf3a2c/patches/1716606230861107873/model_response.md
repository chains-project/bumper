```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Map<String, String> extraProperties = globalConfig.extraProperties();
    Properties properties = new Properties();
    properties.putAll(extraProperties);
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(properties)
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```