Here's the proposed patch:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalRepositories.loadLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

This patch creates a new variable `languageSupportRepository` to get the enabled languages from the new method `getEnabledLanguagesInConnectedMode()` in the `LanguageSupportRepository` class.