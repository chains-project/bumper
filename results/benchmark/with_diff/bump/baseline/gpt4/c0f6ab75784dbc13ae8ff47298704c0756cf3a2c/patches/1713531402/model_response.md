```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = new LanguageSupportRepository();
    Set<Language> enabledLanguages = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
    
    return AnalysisEngineConfiguration.builder()
            .setEnabledLanguages(enabledLanguages)
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```