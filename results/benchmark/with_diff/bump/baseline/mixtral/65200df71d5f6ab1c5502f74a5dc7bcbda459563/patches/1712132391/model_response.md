Here's the proposed patch:

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

Changes made:

* Created a variable `languageSupportRepository` to hold an instance of `LanguageSupportRepository`.
* Replaced the call to `getEnabledLanguages()` with `setEnabledLanguages()` and passed `languageSupportRepository.getEnabledLanguagesInConnectedMode()` as an argument.

Note: The assumption here is that the configuration should be built using the languages enabled in connected mode. If that's not the case, you might want to use `getEnabledLanguagesInStandaloneMode()` instead.