```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = globalConfig.getLanguageSupportRepository();
    Set<Language> enabledLanguages;
    if (globalConfig.isConnectedMode()) {
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
Please note that the changes made here are based on assumptions about the globalConfig object. In the real-world application, you might need to adjust the code to correctly access the LanguageSupportRepository and check whether you are in connected mode or standalone mode.