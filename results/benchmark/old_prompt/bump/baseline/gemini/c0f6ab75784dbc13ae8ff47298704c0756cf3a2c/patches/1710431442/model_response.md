```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Map<String, String> extraProperties = globalConfig.extraProperties();
        if (extraProperties == null) {
            extraProperties = new HashMap<>();
        }
        extraProperties.put("sonar.log.level", "DEBUG");
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(extraProperties)
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```