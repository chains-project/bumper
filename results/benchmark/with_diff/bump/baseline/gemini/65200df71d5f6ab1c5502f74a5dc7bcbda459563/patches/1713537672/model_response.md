```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(enabledLanguages)
            .build();
}
```