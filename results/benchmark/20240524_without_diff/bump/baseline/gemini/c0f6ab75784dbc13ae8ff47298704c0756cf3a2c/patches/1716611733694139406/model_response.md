```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        var builder = AnalysisEngineConfiguration.builder();
        builder.addEnabledLanguages(globalConfig.getEnabledLanguages());
        builder.setClientPid(globalConfig.getClientPid());
        builder.setExtraProperties(globalConfig.extraProperties());
        builder.setWorkDir(globalConfig.getWorkDir());
        builder.setModulesProvider(globalConfig.getModulesProvider());
        return builder.build();
    }
```