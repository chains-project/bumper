```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = new HashSet<>();
        if (globalConfig.getEnabledLanguages() != null) {
            enabledLanguages.addAll(globalConfig.getEnabledLanguages());
        }
        if (globalConfig.getMode() == Mode.CONNECTED) {
            enabledLanguages.addAll(LanguageSupportRepository.getEnabledLanguagesInConnectedMode());
        } else {
            enabledLanguages.addAll(LanguageSupportRepository.getEnabledLanguagesInStandaloneMode());
        }
        return AnalysisEngineConfiguration.builder()
                .enabledLanguages(enabledLanguages)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```