```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepo = new LanguageSupportRepository();
    Set<Language> enabledLanguages;

    if (globalConfig.isInConnectedMode()) {
        enabledLanguages = languageSupportRepo.getEnabledLanguagesInConnectedMode();
    } else {
        enabledLanguages = languageSupportRepo.getEnabledLanguagesInStandaloneMode();
    }

    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```