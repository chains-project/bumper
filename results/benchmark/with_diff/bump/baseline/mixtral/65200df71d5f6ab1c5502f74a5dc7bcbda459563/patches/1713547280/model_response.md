Here's the proposed patch for the failing method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalComponentProvider.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we're using the new `LanguageSupportRepository` class to get the enabled languages instead of the deprecated `AnalysisEngineConfiguration` method. We're also setting the client pid, extra properties, work dir, and modules provider the same way as before.