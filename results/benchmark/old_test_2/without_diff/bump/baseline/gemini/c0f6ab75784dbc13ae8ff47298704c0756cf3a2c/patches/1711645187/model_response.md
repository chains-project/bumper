```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfigurationBuilder builder = AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
        if (globalConfig.getModulesProvider() != null) {
            builder.setModulesProvider(globalConfig.getModulesProvider());
        }
        return builder.build();
    }
```