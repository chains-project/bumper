```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        if (globalConfig.isStandalone()) {
            enabledLanguages = globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode();
        } else {
            enabledLanguages = globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInConnectedMode();
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