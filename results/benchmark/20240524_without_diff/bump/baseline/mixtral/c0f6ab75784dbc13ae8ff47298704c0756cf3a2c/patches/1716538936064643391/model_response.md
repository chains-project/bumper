Here is a possible patch for the code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalConfig.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

This patch creates a new variable `languageSupportRepository` to hold an instance of `LanguageSupportRepository`, which has the `getEnabledLanguagesInConnectedMode()` method. This method can be used to get the enabled languages for the analysis engine configuration. The `addEnabledLanguages()` method is no longer needed and has been removed from the library.

Note that this patch assumes that the analysis engine is being used in connected mode. If it is being used in standalone mode, you would need to use the `getEnabledLanguagesInStandaloneMode()` method instead.