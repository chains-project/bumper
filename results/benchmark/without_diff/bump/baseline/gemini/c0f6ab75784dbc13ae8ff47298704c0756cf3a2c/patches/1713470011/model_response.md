```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        final List<String> enabledLanguages = globalConfig.getEnabledLanguages();
        final String clientPid = globalConfig.getClientPid();
        final Map<String, String> extraProperties = globalConfig.extraProperties();
        final File workDir = globalConfig.getWorkDir();
        final ModulesProvider modulesProvider = globalConfig.getModulesProvider();

        return AnalysisEngineConfiguration.builder()
                .enabledLanguages(enabledLanguages)
                .clientPid(clientPid)
                .extraProperties(extraProperties)
                .workDir(workDir)
                .modulesProvider(modulesProvider)
                .build();
    }
```