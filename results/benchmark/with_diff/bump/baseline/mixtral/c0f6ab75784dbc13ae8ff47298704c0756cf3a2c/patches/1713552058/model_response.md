Here's the proposed patch for the `buildAnalysisEngineConfiguration()` method:

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

This patch creates a `LanguageSupportRepository` instance from the global repositories and uses the new method `getEnabledLanguagesInConnectedMode()` to set the enabled languages. Note that I've removed the `addEnabledLanguages()` method call since it is no longer available in the new library version.