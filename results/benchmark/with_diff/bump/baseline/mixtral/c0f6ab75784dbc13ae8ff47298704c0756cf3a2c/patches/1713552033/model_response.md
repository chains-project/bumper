Here is the proposed patch:

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

In this patch, we first get the `LanguageSupportRepository` from `GlobalConfig`. Then, we use the new method `getEnabledLanguagesInConnectedMode()` to get the enabled languages instead of the removed method `getEnabledLanguages()`.