```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = null;
        if (globalConfig.isStandaloneMode()) {
            enabledLanguages = globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode();
        } else {
            enabledLanguages = globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInConnectedMode();
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