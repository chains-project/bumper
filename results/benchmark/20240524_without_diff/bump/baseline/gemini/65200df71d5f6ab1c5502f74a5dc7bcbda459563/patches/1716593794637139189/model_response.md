```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        List<String> enabledLanguages = globalConfig.getEnabledLanguages();
        String clientPid = globalConfig.getClientPid();
        Map<String, String> extraProperties = globalConfig.extraProperties();
        File workDir = globalConfig.getWorkDir();
        ModulesProvider modulesProvider = globalConfig.getModulesProvider();
        return AnalysisEngineConfiguration.builder()
                .setEnabledLanguages(enabledLanguages)
                .setClientPid(clientPid)
                .setExtraProperties(extraProperties)
                .setWorkDir(workDir)
                .setModulesProvider(modulesProvider)
                .build();
    }
```