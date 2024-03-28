```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfigurationBuilder builder = AnalysisEngineConfiguration.builder();
        for (String enabledLanguage : globalConfig.getEnabledLanguages()) {
            builder.addEnabledLanguage(enabledLanguage);
        }
        builder.setClientPid(globalConfig.getClientPid());
        builder.setExtraProperties(globalConfig.extraProperties());
        builder.setWorkDir(globalConfig.getWorkDir());
        builder.setModulesProvider(globalConfig.getModulesProvider());
        return builder.build();
    }
```