```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        for (String language : globalConfig.getEnabledLanguages()) {
            builder.addEnabledLanguage(language);
        }
        builder.setClientPid(globalConfig.getClientPid());
        builder.setExtraProperties(globalConfig.extraProperties());
        builder.setWorkDir(globalConfig.getWorkDir());
        builder.setModulesProvider(globalConfig.getModulesProvider());
        return builder.build();
    }
```