```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration(
      GlobalConfig globalConfig) {
        return AnalysisEngineConfiguration.newBuilder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```