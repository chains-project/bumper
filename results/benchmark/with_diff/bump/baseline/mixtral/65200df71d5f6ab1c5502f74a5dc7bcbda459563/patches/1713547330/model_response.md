Here's the proposed patch for the failing code:

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

In this patch, we create a new variable `languageSupportRepository` to hold an instance of `LanguageSupportRepository`. We then use the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages from this repository. This method was added in the new library version and should be available for use.

Note that we removed the call to `addEnabledLanguages()`, as it is no longer available in the new library version. Instead, we set the enabled languages directly using the new method.