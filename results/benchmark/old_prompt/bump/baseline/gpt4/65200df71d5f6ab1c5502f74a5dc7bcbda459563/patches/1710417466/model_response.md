```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
    if (globalConfig.getEnabledLanguages() != null) {
        builder = builder.addEnabledLanguages(globalConfig.getEnabledLanguages());
    }
    if (globalConfig.getClientPid() != null) {
        builder = builder.setClientPid(globalConfig.getClientPid());
    }
    if (globalConfig.extraProperties() != null) {
        builder = builder.setExtraProperties(globalConfig.extraProperties());
    }
    if (globalConfig.getWorkDir() != null) {
        builder = builder.setWorkDir(globalConfig.getWorkDir());
    }
    if (globalConfig.getModulesProvider() != null) {
        builder = builder.setModulesProvider(globalConfig.getModulesProvider());
    }
    return builder.build();
}
```