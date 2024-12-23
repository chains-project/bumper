```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        boolean connectedMode = globalConfig.getConnectedMode();

        Set<Language> languages;
        if (connectedMode) {
            languages = LanguageSupportRepository.getEnabledLanguagesInConnectedMode();
        } else {
            languages = LanguageSupportRepository.getEnabledLanguagesInStandaloneMode();
        }

        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(languages)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```