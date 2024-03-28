```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        ModulesProvider modulesProvider = globalConfig.getModulesProvider();
        if (modulesProvider == null) {
            modulesProvider = new ModulesProvider();
        }
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(modulesProvider)
                .build();
    }
```