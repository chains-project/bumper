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

This patch uses the new method `getEnabledLanguagesInConnectedMode()` from `LanguageSupportRepository` to get the enabled languages, instead of using the deprecated method from `AnalysisEngineConfiguration`. The `LanguageSupportRepository` is obtained through `GlobalRepositories.getLanguageSupportRepository()`.