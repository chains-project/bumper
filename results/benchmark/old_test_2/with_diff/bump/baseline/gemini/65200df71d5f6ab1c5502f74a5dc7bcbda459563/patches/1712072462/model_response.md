```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
        Set<Language> enabledLanguagesInConnectedMode = languageSupportRepository.getEnabledLanguagesInConnectedMode();
        Set<Language> enabledLanguagesInStandaloneMode = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguagesInConnectedMode)
                .addEnabledLanguages(enabledLanguagesInStandaloneMode)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```