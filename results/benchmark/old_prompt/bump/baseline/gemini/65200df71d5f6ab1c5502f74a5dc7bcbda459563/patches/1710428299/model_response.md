```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Map<String, Object> properties = new HashMap<>();
        properties.putAll(globalConfig.extraProperties());
        properties.put(AnalysisEngineConfiguration.ENABLED_LANGUAGES, globalConfig.getEnabledLanguages());
        properties.put(AnalysisEngineConfiguration.CLIENT_PID, globalConfig.getClientPid());
        properties.put(AnalysisEngineConfiguration.WORK_DIR, globalConfig.getWorkDir());
        properties.put(AnalysisEngineConfiguration.MODULES_PROVIDER, globalConfig.getModulesProvider());
        return AnalysisEngineConfiguration.builder().setProperties(properties).build();
    }
```