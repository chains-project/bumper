Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setLanguageSupportRepository(new LanguageSupportRepository())
                .build();
    }
```
The patch creates a new instance of `LanguageSupportRepository` and sets it to the `AnalysisEngineConfiguration` builder using the `setLanguageSupportRepository` method. This allows the `addEnabledLanguages` method to be called on the `LanguageSupportRepository` instance, which is now available in the updated library version.

The `LanguageSupportRepository` class has two methods for getting enabled languages: `getEnabledLanguagesInConnectedMode` and `getEnabledLanguagesInStandaloneMode`. These methods can be called instead of the removed `getEnabledLanguages` method.

By adding this patch, the code should now compile and work with the updated library version.