Here's a possible patch for the code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalRepositoryFactory.createGlobalRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we create a `LanguageSupportRepository` instance and use it to get the enabled languages for connected mode instead of using `globalConfig`. Note that the new library version has added two methods for getting enabled languages in connected and standalone modes. We use the one for connected mode (`getEnabledLanguagesInConnectedMode()`) because it seems more appropriate for the analysis engine configuration.