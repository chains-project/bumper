```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
        if (languageSupportRepository.isStandaloneMode()) {
            builder.addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInStandaloneMode());
        } else {
            builder.addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode());
        }
        return builder.build();
    }
```