```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageRepo = new LanguageSupportRepository();
    Set<Language> enabledLanguages = globalConfig.isInConnectedMode() ? 
        languageRepo.getEnabledLanguagesInConnectedMode() : 
        languageRepo.getEnabledLanguagesInStandaloneMode();
        
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```