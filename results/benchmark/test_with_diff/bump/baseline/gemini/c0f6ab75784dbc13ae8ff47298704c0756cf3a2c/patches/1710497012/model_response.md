```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
        return AnalysisEngineConfiguration.builder()
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setClientPid(globalConfig.getClientPid())
                .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInStandaloneMode())
                .build();
    }
```