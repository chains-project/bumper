Here's the patched version of the `buildAnalysisEngineConfiguration` method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = globalConfig.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

Note that I replaced the `addEnabledLanguages` method with `setEnabledLanguages` and used the new method `getEnabledLanguagesInConnectedMode` from the `LanguageSupportRepository`.