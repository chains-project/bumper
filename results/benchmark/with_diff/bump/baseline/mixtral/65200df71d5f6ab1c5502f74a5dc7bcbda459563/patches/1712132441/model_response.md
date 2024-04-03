Sure, here's a possible patch for the code to fix the error:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = globalConfig.getLanguageSupportRepository();
    return AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
            .build();
}
```

In this patch, we first get the `LanguageSupportRepository` object from `globalConfig`. Then, instead of calling `getEnabledLanguages()`, we call `getEnabledLanguagesInConnectedMode()` to get the enabled languages. This should fix the "cannot find symbol" error.

Note that this patch assumes that the enabled languages in connected mode are the same as the enabled languages in the original code. If this is not the case, you may need to modify the patch accordingly.