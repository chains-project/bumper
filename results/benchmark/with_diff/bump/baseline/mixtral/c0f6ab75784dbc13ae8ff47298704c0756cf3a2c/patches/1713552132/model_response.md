Here's the proposed patch for the failing method:

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

This patch creates a new variable `languageSupportRepository` to get the `LanguageSupportRepository` instance from `GlobalConfig`. It then uses the new method `getEnabledLanguagesInConnectedMode()` to set the enabled languages for the `AnalysisEngineConfiguration`.