```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getService(LanguageSupportRepository.class);
        Set<Language> enabledLanguagesInConnectedMode = languageSupportRepository.getEnabledLanguagesInConnectedMode();
        Set<Language> enabledLanguagesInStandaloneMode = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
        Set<Language> enabledLanguages = new HashSet<>(enabledLanguagesInConnectedMode);
        enabledLanguages.addAll(enabledLanguagesInStandaloneMode);
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguages)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```