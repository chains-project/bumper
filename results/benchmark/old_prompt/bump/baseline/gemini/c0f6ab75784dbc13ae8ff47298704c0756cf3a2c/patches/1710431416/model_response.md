```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        ModulesProvider modulesProvider = globalConfig.getModulesProvider();
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        builder.addEnabledLanguages(globalConfig.getEnabledLanguages());
        builder.setClientPid(globalConfig.getClientPid());
        builder.setExtraProperties(globalConfig.extraProperties());
        builder.setWorkDir(globalConfig.getWorkDir());
        if (modulesProvider != null) {
            builder.setModulesProvider(modulesProvider);
        }
        return builder.build();
    }
```