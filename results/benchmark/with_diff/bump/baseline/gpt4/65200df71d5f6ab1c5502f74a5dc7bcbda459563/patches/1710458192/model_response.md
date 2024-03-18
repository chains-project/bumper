```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = globalConfig.getLanguageSupportRepository();
    Set<Language> enabledLanguages;
    if (globalConfig.isInConnectedMode()) {
        enabledLanguages = languageSupportRepository.getEnabledLanguagesInConnectedMode();
    } else {
        enabledLanguages = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
    }
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```
This solution assumes that there's a method in `globalConfig` to determine whether we are in connected mode or standalone mode. If such a method doesn't exist, you'll need to determine that some other way. It also assumes that `globalConfig` has a method to get the `LanguageSupportRepository`. If it doesn't, you'll need to get that some other way as well.