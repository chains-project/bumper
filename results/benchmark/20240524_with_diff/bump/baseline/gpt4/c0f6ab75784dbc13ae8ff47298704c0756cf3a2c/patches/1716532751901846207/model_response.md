```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = new LanguageSupportRepository();
    Set<Language> enabledLanguages = null;
    if(globalConfig.isInConnectedMode()) {
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
