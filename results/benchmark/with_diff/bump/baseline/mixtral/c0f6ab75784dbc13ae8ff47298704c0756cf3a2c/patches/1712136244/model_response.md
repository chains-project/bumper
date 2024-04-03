Sure, here's a possible patch for the failing code:
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
In this patch, we first get the `LanguageSupportRepository` from the `globalConfig` object. We then use the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages, and pass it to the `AnalysisEngineConfiguration.Builder`.

Note that we no longer use the `addEnabledLanguages()` method, since it has been removed in the new library version. Instead, we use the new method `setEnabledLanguages()` to set the enabled languages.

Also, we assume that the `globalConfig` object has a new method `getLanguageSupportRepository()` that returns the `LanguageSupportRepository` object. If this method is not available, you may need to modify the code accordingly.