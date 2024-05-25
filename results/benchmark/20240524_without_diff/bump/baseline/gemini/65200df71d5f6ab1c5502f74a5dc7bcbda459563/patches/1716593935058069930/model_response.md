```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        List<String> enabledLanguages = globalConfig.getEnabledLanguages();
        String clientPid = globalConfig.getClientPid();
        Map<String, String> extraProperties = globalConfig.extraProperties();
        String workDir = globalConfig.getWorkDir();
        ModulesProvider modulesProvider = globalConfig.getModulesProvider();
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        builder.addEnabledLanguages(enabledLanguages);
        builder.setClientPid(clientPid);
        builder.setExtraProperties(extraProperties);
        builder.setWorkDir(workDir);
        builder.setModulesProvider(modulesProvider);
        return builder.build();
    }
```