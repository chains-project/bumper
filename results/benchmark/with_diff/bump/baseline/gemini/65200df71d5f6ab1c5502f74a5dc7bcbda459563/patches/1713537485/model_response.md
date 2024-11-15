```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getLanguageSupportRepository();
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();

    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .addEnabledLanguages(
                    enabledLanguages.isEmpty()
                            ? languageSupportRepository.getEnabledLanguagesInStandaloneMode()
                            : languageSupportRepository.getEnabledLanguagesInConnectedMode()
            )
            .build();
}
```