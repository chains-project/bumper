```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    List<String> enabledLanguages = globalConfig.getEnabledLanguages();
    String clientPid = globalConfig.getClientPid();
    Map<String, String> extraProperties = globalConfig.extraProperties();
    File workDir = globalConfig.getWorkDir();
    ModulesProvider modulesProvider = globalConfig.getModulesProvider();

    AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
    builder.setClientPid(clientPid);
    builder.setWorkDir(workDir);
    builder.setModulesProvider(modulesProvider);
    builder.setExtraProperties(extraProperties);
    builder.setEnabledLanguages(enabledLanguages);

    return builder.build();
  }
```