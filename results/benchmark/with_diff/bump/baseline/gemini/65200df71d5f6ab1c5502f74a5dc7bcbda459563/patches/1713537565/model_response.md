```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<Language> enabledLanguages = new HashSet<>();
    if (globalConfig.isStandaloneMode()) {
        enabledLanguages.addAll(LanguageSupportRepository.getEnabledLanguagesInStandaloneMode());
    } else {
        enabledLanguages.addAll(LanguageSupportRepository.getEnabledLanguagesInConnectedMode());
    }
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(enabledLanguages)
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```