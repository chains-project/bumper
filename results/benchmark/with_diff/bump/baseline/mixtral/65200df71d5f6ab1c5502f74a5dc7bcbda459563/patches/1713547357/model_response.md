Here is a possible patch for the code:

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

The changes I made are:

* I removed the line `.addEnabledLanguages(globalConfig.getEnabledLanguages())` because it is causing the error.
* I added a new line `LanguageSupportRepository languageSupportRepository = GlobalRepositories.getLanguageSupportRepository();` to get an instance of `LanguageSupportRepository`.
* I added a new line `.setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())` to set the enabled languages for the analysis engine configuration.

I hope this helps! Let me know if you have any questions.