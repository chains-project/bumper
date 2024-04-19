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

In this patch, I've removed the `addEnabledLanguages` method call and replaced it with a new variable `languageSupportRepository` which is initialized with `GlobalConfig.getLanguageSupportRepository()`. Then, I've used the new method `getEnabledLanguagesInConnectedMode()` of `LanguageSupportRepository` to set the enabled languages in the `AnalysisEngineConfiguration.Builder`.

Note that I've assumed that the `GlobalConfig` class has a method `getLanguageSupportRepository()` to get an instance of `LanguageSupportRepository`. If that's not the case, you may need to modify the code accordingly.