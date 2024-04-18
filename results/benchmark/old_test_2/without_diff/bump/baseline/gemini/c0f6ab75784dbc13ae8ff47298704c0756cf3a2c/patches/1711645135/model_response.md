```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfigurationBuilder builder = AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
        ++builder.setAnalysisEngineClassLoader(globalConfig.getAnalysisEngineClassLoader());
        return builder.build();
    }
```