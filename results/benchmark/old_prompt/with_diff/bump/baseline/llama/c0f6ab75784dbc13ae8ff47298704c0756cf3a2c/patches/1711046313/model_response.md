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
We removed the `getEnabledLanguages()` method call, which is no longer available in the updated library version. Instead, we use the `LanguageSupportRepository.getEnabledLanguagesInConnectedMode()` method, which is a new addition in the updated library version. This method returns a `java.util.Set` object, which can be directly passed to the `addEnabledLanguages()` method.

By making this change, we're ensuring that the code compiles and runs correctly with the updated library version.