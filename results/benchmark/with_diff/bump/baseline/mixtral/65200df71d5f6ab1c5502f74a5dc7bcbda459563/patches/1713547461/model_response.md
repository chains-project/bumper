Here is a possible patch for the code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = GlobalComponentProvider.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we use the new method `LanguageSupportRepository.getEnabledLanguagesInConnectedMode()` to get the enabled languages, instead of the deprecated method `AnalysisEngineConfiguration.getEnabledLanguages()`. We also use the `LanguageSupportRepository` instance provided by the `GlobalComponentProvider`.

Note that the `addEnabledLanguages()` method is not available anymore, so we use the `setEnabledLanguages()` method instead. This method sets the enabled languages, replacing any previous value. If you want to add languages to the existing ones, you can use the `addEnabledLanguages()` method from the `LanguageSupportRepository` class.

I hope this helps! Let me know if you have any other questions.