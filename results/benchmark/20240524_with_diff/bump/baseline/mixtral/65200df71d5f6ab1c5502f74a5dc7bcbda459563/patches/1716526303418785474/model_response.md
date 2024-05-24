Here's a possible patch that you can apply to the code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalRepositoryStorage.instance().get(LanguageSupportRepository.class);
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we first retrieve a `LanguageSupportRepository` instance from the `GlobalRepositoryStorage`. We then use the new `getEnabledLanguagesInConnectedMode()` method of this repository to get the set of enabled languages.

Note that we have removed the call to `addEnabledLanguages()`, since it is no longer available in the new version of the library. Instead, we set the enabled languages directly using the new method.

Additionally, we have assumed that the code should use the set of enabled languages in connected mode. If the code should use the set of enabled languages in standalone mode instead, you can simply replace `getEnabledLanguagesInConnectedMode()` with `getEnabledLanguagesInStandaloneMode()`.