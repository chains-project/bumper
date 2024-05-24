```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        boolean standaloneMode = globalConfig.isStandaloneMode();
        Set<Language> enabledLanguagesInMode = standaloneMode
                ? LanguageSupportRepository.getEnabledLanguagesInStandaloneMode()
                : LanguageSupportRepository.getEnabledLanguagesInConnectedMode();
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguagesInMode)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```