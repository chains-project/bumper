Here is a possible patch for the failing code:
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
Explanation:

* We create a new variable `languageSupportRepository` to hold an instance of `LanguageSupportRepository`, which provides the new methods for getting the enabled languages.
* We remove the call to `addEnabledLanguages()`, which is no longer available in the new version of `AnalysisEngineConfiguration.Builder`.
* We add a call to `setEnabledLanguages()`, passing the set of enabled languages obtained from `languageSupportRepository`.
* We assume that `GlobalConfig.getLanguageSupportRepository()` returns an instance of `LanguageSupportRepository` that provides the new methods for getting the enabled languages. If this assumption is incorrect, you may need to modify the code accordingly.