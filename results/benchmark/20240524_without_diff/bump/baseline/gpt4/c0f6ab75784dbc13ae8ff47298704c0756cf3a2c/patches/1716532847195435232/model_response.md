```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = new LanguageSupportRepository();
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages().stream()
        .map(Language::new)
        .collect(Collectors.toSet());
    languageSupportRepository.getEnabledLanguagesInConnectedMode().addAll(enabledLanguages);
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```