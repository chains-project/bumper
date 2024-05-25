```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        List<String> enabledLanguages = globalConfig.getEnabledLanguages();
        String clientPid = globalConfig.getClientPid();
        Map<String, String> extraProperties = globalConfig.extraProperties();
        File workDir = globalConfig.getWorkDir();
        ModulesProvider modulesProvider = globalConfig.getModulesProvider();
        return AnalysisEngineConfiguration.builder()
                .enabledLanguages(enabledLanguages)
                .clientPid(clientPid)
                .extraProperties(extraProperties)
                .workDir(workDir)
                .modulesProvider(modulesProvider)
                .build();
    }
```