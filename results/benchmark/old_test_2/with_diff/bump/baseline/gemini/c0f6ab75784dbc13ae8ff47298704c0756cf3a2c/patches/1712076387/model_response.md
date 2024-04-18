```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getInstance(LanguageSupportRepository.class);
        Set<Language> enabledLanguages = languageSupportRepository.getEnabledLanguagesInConnectedMode();
        if (enabledLanguages == null || enabledLanguages.isEmpty()) {
            enabledLanguages = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
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