```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Map<String, String> extraProperties = new HashMap<>();
        extraProperties.putAll(globalConfig.extraProperties());
        extraProperties.put(AnalysisEngineConfiguration.OPTION_WORK_DIR, globalConfig.getWorkDir());
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(extraProperties)
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```