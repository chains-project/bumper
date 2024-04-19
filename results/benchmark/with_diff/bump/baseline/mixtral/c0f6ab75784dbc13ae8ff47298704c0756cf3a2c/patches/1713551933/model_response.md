Here's the proposed patch for the `buildAnalysisEngineConfiguration()` method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalRepositoryStorage.getInstance().getRepository(LanguageSupportRepository.KEY);
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

The patch replaces the `addEnabledLanguages()` method with `setEnabledLanguages()` and uses the new method `getEnabledLanguagesInConnectedMode()` from `LanguageSupportRepository`. Additionally, the `LanguageSupportRepository` instance is obtained from the `GlobalRepositoryStorage`.