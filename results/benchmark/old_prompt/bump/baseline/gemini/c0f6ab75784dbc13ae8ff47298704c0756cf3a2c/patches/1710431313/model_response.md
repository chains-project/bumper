```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        ModulesProvider modulesProvider = globalConfig.getModulesProvider();
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(modulesProvider != null ? modulesProvider : ModulesProvider.EMPTY)
                .build();
    }
```