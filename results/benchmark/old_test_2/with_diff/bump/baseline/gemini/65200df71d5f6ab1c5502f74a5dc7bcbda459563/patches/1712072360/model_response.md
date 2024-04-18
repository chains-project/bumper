```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().get(LanguageSupportRepository.class);
        Set<Language> enabledLanguages = languageSupportRepository.getEnabledLanguagesInConnectedMode();
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguages)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```