```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
        return AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
                .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInStandaloneMode())
                .build();
    }
```