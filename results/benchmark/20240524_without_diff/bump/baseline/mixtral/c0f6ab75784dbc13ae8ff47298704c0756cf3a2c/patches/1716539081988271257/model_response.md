Here is a possible patch for the failing code:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageRepository = GlobalConfig.getLanguageRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```
In this patch, I created a new variable `languageRepository` to hold an instance of `LanguageSupportRepository`. I then used the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages. This method was added in the new library version and can be used to replace the removed method `getEnabledLanguages()`.

Note that I assumed that `GlobalConfig` has a method `getLanguageRepository()` that returns an instance of `LanguageSupportRepository`. If this is not the case, you may need to modify the code accordingly.