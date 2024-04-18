```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getModule(LanguageSupportRepository.class);
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```