```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        Set<LanguageSupportRepository.Language> enabledLanguagesInConnectedMode = new HashSet<>();
        Set<LanguageSupportRepository.Language> enabledLanguagesInStandaloneMode = new HashSet<>();
        for (Language language : enabledLanguages) {
            enabledLanguagesInConnectedMode.add(LanguageSupportRepository.Language.valueOf(language.name()));
            enabledLanguagesInStandaloneMode.add(LanguageSupportRepository.Language.valueOf(language.name()));
        }
        return AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setEnabledLanguagesInConnectedMode(enabledLanguagesInConnectedMode)
                .setEnabledLanguagesInStandaloneMode(enabledLanguagesInStandaloneMode)
                .build();
    }
```