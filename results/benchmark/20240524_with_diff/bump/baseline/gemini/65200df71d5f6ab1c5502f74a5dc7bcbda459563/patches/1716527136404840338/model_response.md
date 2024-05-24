```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
    boolean standaloneMode = globalConfig.isStandaloneMode();
    Set<Language> languagesInMode = standaloneMode ?
            LanguageSupportRepository.getEnabledLanguagesInStandaloneMode() :
            LanguageSupportRepository.getEnabledLanguagesInConnectedMode();

    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(enabledLanguages.stream().filter(languagesInMode::contains).collect(Collectors.toSet()))
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```