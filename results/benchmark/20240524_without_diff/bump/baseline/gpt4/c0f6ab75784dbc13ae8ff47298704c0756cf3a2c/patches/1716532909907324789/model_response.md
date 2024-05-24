```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = new LanguageSupportRepository();
    
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages().stream()
        .map(language -> languageSupportRepository.getEnabledLanguagesInConnectedMode()
            .stream()
            .filter(enabledLanguage -> enabledLanguage.equals(language))
            .findFirst()
            .orElse(null))
        .filter(Objects::nonNull)
        .collect(Collectors.toSet());

    return AnalysisEngineConfiguration.builder()
        .setClientPid(globalConfig.getClientPid())
        .setExtraProperties(globalConfig.extraProperties())
        .setWorkDir(globalConfig.getWorkDir())
        .setModulesProvider(globalConfig.getModulesProvider())
        .build();
}
```