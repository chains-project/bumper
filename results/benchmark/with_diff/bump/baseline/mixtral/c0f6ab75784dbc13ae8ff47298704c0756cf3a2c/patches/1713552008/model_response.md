Here is a possible patch for the failing code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalRepositories.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we first get a reference to the `LanguageSupportRepository` object, which provides the new `getEnabledLanguagesInConnectedMode()` method. We then use this method to get the set of enabled languages, instead of calling `getEnabledLanguages()` on the `AnalysisEngineConfiguration.Builder`.

Note that this patch assumes that the client code is running in connected mode. If the client code can also run in standalone mode, you may need to modify the patch to use `getEnabledLanguagesInStandaloneMode()` instead, depending on your specific requirements.