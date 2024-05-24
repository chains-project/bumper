Here's the fixed version of the method using the added `LanguageSupportRepository` class:

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

This version uses the new `LanguageSupportRepository` class to obtain the enabled languages. Note that I made the assumption that `globalConfig` is an instance of `GlobalConfiguration`. If it's not, you might need to adjust the code accordingly.