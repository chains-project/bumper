```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        if (globalConfig.isStandaloneMode()) {
            builder.addEnabledLanguages(LanguageSupportRepository.getEnabledLanguagesInStandaloneMode());
        } else {
            builder.addEnabledLanguages(LanguageSupportRepository.getEnabledLanguagesInConnectedMode());
        }
        for (Language language : enabledLanguages) {
            builder.addEnabledLanguage(language);
        }
        builder.setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
        return builder.build();
    }
```