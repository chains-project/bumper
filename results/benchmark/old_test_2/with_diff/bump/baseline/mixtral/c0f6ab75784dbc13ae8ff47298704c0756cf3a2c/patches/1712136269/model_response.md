Here is the proposed patch:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalConfiguration.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

This patch creates a new variable `languageSupportRepository` to hold an instance of `LanguageSupportRepository`, which has the new `getEnabledLanguagesInConnectedMode()` method. This method is used instead of `getEnabledLanguages()` to set the enabled languages for the analysis engine configuration. The other settings are unchanged.