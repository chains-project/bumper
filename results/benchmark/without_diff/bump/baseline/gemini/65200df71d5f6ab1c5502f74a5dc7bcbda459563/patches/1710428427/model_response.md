```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Map<String, String> extraProperties = globalConfig.extraProperties();
        extraProperties.put("sonar.analysis.language", globalConfig.getEnabledLanguages());
        extraProperties.put("sonar.analysis.clientPid", globalConfig.getClientPid());
        extraProperties.put("sonar.analysis.workDir", globalConfig.getWorkDir());
        extraProperties.put("sonar.analysis.modulesProvider", globalConfig.getModulesProvider());
        return AnalysisEngineConfiguration.builder()
                .setExtraProperties(extraProperties)
                .build();
    }
```