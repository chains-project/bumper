```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration(Config globalConfig) {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setClassLoader(globalConfig.getClassLoader())
                .build();
    }
```