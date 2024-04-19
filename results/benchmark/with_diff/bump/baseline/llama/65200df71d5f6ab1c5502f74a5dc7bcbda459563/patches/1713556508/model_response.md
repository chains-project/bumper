Here's a possible patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(LanguageSupportRepository.getEnabledLanguagesInConnectedMode())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .build();
}
```
This patch removes the call to `globalConfig.getEnabledLanguages()` and instead uses the `LanguageSupportRepository.getEnabledLanguagesInConnectedMode()` method to get the list of enabled languages. This method was added in the new version of the library, and it returns a set of languages that are enabled in connected mode.

By using this method, we avoid the issue of the removed `getEnabledLanguages()` method and ensure that the code compiles and runs correctly with the new version of the library.