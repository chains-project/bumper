```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        
        if (languageSupportRepository.isConnectedMode()) {
            enabledLanguages = languageSupportRepository.getEnabledLanguagesInConnectedMode();
        } else {
            enabledLanguages = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
        }

        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguages)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```