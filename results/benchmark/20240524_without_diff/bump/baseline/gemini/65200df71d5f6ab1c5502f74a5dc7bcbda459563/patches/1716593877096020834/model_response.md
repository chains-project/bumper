```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        builder.setClientPid(globalConfig.getClientPid());
        builder.setWorkDir(globalConfig.getWorkDir());
        builder.setModulesProvider(globalConfig.getModulesProvider());
        builder.setExtraProperties(globalConfig.extraProperties());
        for (String enabledLanguage : globalConfig.getEnabledLanguages()) {
            builder.addEnabledLanguage(enabledLanguage);
        }
        return builder.build();
    }
```