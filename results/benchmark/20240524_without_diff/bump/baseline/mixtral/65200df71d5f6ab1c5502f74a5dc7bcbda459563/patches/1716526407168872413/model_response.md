Here is the proposed patch:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalRepositoryFactory.createGlobalRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we create a `LanguageSupportRepository` instance to get the enabled languages for connected mode. We then pass this set of languages to the `AnalysisEngineConfiguration.Builder` using the new method `setEnabledLanguages`.

Note that the `addEnabledLanguages` method has been removed in the new library version, so we replace it with the new method `setEnabledLanguages`. Also, we remove the call to `globalConfig.getEnabledLanguages()` since it is no longer needed.