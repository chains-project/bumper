```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = new LanguageSupportRepository();
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInStandaloneMode(enabledLanguages))
            .build();
}
```