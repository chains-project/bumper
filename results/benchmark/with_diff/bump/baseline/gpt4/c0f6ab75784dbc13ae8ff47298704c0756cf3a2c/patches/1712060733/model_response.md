```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = globalConfig.getLanguageSupportRepository();
    Set<Language> enabledLanguages;
    
    if (globalConfig.isInConnectedMode()) {
        enabledLanguages = languageSupportRepository.getEnabledLanguagesInConnectedMode();
    } else {
        enabledLanguages = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
    }

    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```
