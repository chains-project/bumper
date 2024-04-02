Here's a proposed patch to fix the error:
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
The patch removes the call to `globalConfig.getEnabledLanguages()` and instead uses the `LanguageSupportRepository.getEnabledLanguagesInConnectedMode()` method to get the list of enabled languages. This method is available in the updated version of the library and can be used to replace the removed `getEnabledLanguages()` method.