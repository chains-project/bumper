```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<Language> enabledLanguages;
    if (globalConfig.isInConnectedMode()) {
        enabledLanguages = LanguageSupportRepository.getEnabledLanguagesInConnectedMode();
    } else {
        enabledLanguages = LanguageSupportRepository.getEnabledLanguagesInStandaloneMode();
    }

    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```