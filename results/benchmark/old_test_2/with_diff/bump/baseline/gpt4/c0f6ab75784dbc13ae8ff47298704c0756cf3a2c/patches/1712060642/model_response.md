```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepo = new LanguageSupportRepository();
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages().stream()
            .map(language -> languageSupportRepo.getEnabledLanguagesInConnectedMode())
            .collect(Collectors.toSet());

    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```