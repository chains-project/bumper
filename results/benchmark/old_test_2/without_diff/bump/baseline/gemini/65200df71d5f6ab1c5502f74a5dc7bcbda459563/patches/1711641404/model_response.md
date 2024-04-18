```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration(final ModuleDescriptorProvider moduleDescriptorProvider) {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(moduleDescriptorProvider)
                .build();
    }
```