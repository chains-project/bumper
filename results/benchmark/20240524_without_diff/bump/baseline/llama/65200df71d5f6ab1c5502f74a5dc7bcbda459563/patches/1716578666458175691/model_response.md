```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Map<String, String> extraProperties = globalConfig.extraProperties();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(extraProperties.isEmpty() ? Collections.emptyMap() : extraProperties)
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```