Here's the proposed patch to fix the error:

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

In this patch, we first get the `LanguageSupportRepository` object from the `GlobalConfiguration`. We then use the new method `getEnabledLanguagesInConnectedMode()` from the `LanguageSupportRepository` to get the enabled languages. Finally, we pass this set of enabled languages to the `AnalysisEngineConfiguration.Builder`.