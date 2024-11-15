```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        return AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setEnabledLanguages(enabledLanguages.stream()
                        .filter(language -> languageSupportRepository.getEnabledLanguagesInConnectedMode().contains(language)
                                || languageSupportRepository.getEnabledLanguagesInStandaloneMode().contains(language))
                        .collect(Collectors.toSet()))
                .build();
    }
```