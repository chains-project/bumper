Here's the proposed patch:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalConfiguration.instance().getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

This patch creates a new variable `languageSupportRepository` to get the enabled languages from the new method `getEnabledLanguagesInConnectedMode()` of the `LanguageSupportRepository` class. The `addEnabledLanguages()` method is removed in the new version, so it is replaced with `setEnabledLanguages()`.