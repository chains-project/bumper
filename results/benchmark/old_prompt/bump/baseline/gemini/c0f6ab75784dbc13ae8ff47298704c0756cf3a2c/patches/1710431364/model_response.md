```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Map<String, String> extraProperties = globalConfig.extraProperties();
        extraProperties.put("sonar.analysis.workdir", globalConfig.getWorkDir());
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(extraProperties)
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```