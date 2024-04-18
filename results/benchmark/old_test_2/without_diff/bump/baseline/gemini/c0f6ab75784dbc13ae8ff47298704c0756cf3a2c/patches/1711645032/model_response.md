```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir());
        ++builder.setModulesProvider(globalConfig.getModulesProvider());
        return builder.build();
    }
```