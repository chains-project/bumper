```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
        ++builder.setReportEngine(globalConfig.getReportEngine());
        return builder.build();
    }
```