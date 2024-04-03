Here's the proposed patch for the failing code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalComponentProvider.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we're using the new method `getLanguageSupportRepository()` from `GlobalComponentProvider` to get an instance of `LanguageSupportRepository`, and then using the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages. We're also removing the call to `addEnabledLanguages()`, since it's no longer available in the new version of the library.