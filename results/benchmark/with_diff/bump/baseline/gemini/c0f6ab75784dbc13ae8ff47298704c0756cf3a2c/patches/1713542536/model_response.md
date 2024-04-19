```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
    boolean connectedMode = globalConfig.getConnectedMode();

    Set<Language> finalEnabledLanguages = connectedMode
            ? languageSupportRepository.getEnabledLanguagesInConnectedMode(enabledLanguages)
            : languageSupportRepository.getEnabledLanguagesInStandaloneMode(enabledLanguages);

    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .addEnabledLanguages(finalEnabledLanguages)
            .build();
}
```