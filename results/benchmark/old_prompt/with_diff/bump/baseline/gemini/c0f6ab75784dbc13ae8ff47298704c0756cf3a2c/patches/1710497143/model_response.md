```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        boolean connectedMode = globalConfig.getConnectedMode();
        Set<Language> enabledLanguagesInMode = connectedMode ?
                globalConfig.getLanguageSupportRepository().getEnabledLanguagesInConnectedMode() :
                globalConfig.getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode();
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguagesInMode)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```