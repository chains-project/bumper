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
The patch removes the call to `globalConfig.getEnabledLanguages()` and instead uses the `LanguageSupportRepository.getEnabledLanguagesInConnectedMode()` method to retrieve the list of enabled languages. This method was added in the new library version, and it returns a set of languages that are enabled in connected mode.

The patch also removes the `Override` annotation, as the method is not overriding any method in the new version.

This patch should fix the error and allow the code to compile and run successfully.