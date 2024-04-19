Here is a possible patch for the code you provided:

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

This patch uses the new `LanguageSupportRepository` class to get the enabled languages instead of the deprecated `AnalysisEngineConfiguration` method. It also removes the `addEnabledLanguages` method call, since it is no longer needed.

Note that this patch assumes that the `GlobalConfiguration` class has a method `getLanguageSupportRepository` that returns a `LanguageSupportRepository` object. If this is not the case, you may need to modify the patch accordingly.