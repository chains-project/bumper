```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepo = new LanguageSupportRepository();
    Set<Language> enabledLanguages = globalConfig.isInConnectedMode()
        ? languageSupportRepo.getEnabledLanguagesInConnectedMode()
        : languageSupportRepo.getEnabledLanguagesInStandaloneMode();
    return AnalysisEngineConfiguration.builder()
        .setClientPid(globalConfig.getClientPid())
        .setExtraProperties(globalConfig.extraProperties())
        .setWorkDir(globalConfig.getWorkDir())
        .setModulesProvider(globalConfig.getModulesProvider())
        .build();
}
```