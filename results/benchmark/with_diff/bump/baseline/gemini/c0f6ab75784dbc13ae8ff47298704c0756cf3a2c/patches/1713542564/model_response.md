```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        if (globalConfig.isStandaloneMode()) {
            enabledLanguages = LanguageSupportRepository.getEnabledLanguagesInStandaloneMode();
        } else {
            enabledLanguages = LanguageSupportRepository.getEnabledLanguagesInConnectedMode();
        }
        return AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .addEnabledLanguages(enabledLanguages)
                .build();
    }
```