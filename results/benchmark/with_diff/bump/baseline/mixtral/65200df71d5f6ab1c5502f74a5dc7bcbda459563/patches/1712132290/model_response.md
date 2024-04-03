Here's the proposed patch for the failing client code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalComponentProvider.getGlobalRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

Note that the `getEnabledLanguages` method has been removed from `AnalysisEngineConfiguration.Builder`, so we need to use the new method `getEnabledLanguagesInConnectedMode` from `LanguageSupportRepository` instead. We can get a reference to the `LanguageSupportRepository` using the `GlobalComponentProvider` class.