Here's the proposed patch to fix the error:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalComponentProvider.getGlobalRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

This patch creates a new variable `languageSupportRepository` to hold an instance of `LanguageSupportRepository`, which has the new methods to get the enabled languages. The `addEnabledLanguages` method has been removed, so we use the new `setEnabledLanguages` method instead. The `getEnabledLanguages` method has also been removed, so we use `getEnabledLanguagesInConnectedMode` instead.