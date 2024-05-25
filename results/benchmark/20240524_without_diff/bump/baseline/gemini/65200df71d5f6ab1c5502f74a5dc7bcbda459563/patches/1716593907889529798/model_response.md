```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        GlobalConfig globalConfig = new GlobalConfig();
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        builder.addEnabledLanguages(globalConfig.getEnabledLanguages());
        builder.setClientPid(globalConfig.getClientPid());
        builder.setExtraProperties(globalConfig.extraProperties());
        builder.setWorkDir(globalConfig.getWorkDir());
        builder.setModulesProvider(globalConfig.getModulesProvider());
        return builder.build();
    }
```