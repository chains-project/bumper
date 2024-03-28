```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .clientPid(globalConfig.getClientPid())
            .extraProperties(globalConfig.extraProperties())
            .workDir(globalConfig.getWorkDir())
            .modulesProvider(globalConfig.getModulesProvider())
            .build();
}
```