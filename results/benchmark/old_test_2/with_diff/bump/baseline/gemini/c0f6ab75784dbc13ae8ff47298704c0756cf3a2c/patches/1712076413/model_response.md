```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        Set<Language> enabledLanguagesInConnectedMode = globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInConnectedMode();
        Set<Language> enabledLanguagesInStandaloneMode = globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode();
        enabledLanguages.addAll(enabledLanguagesInConnectedMode);
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