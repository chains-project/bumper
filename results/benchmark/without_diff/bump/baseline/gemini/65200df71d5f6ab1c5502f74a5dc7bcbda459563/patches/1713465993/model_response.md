```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration(GlobalConfig globalConfig) {
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        builder.enabledLanguages(globalConfig.getEnabledLanguages());
        builder.clientPid(globalConfig.getClientPid());
        builder.extraProperties(globalConfig.extraProperties());
        builder.workDir(globalConfig.getWorkDir());
        builder.modulesProvider(globalConfig.getModulesProvider());
        return builder.build();
    }
```