```
    private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setLanguageSupportRepository(new LanguageSupportRepository()) //add this line
                .build();
    }
```
This patch creates a new instance of `LanguageSupportRepository` and sets it to the `AnalysisEngineConfiguration` using the `setLanguageSupportRepository` method. This allows the `AnalysisEngineConfiguration` to use the `LanguageSupportRepository` to get the enabled languages, instead of the removed `getEnabledLanguages` method.

The `LanguageSupportRepository` class has two methods to get the enabled languages, `getEnabledLanguagesInConnectedMode` and `getEnabledLanguagesInStandaloneMode`, which can be used depending on the mode the application is running in.

This patch does not modify the signature of the `buildAnalysisEngineConfiguration` method, and it only adds a single line of code to set the `LanguageSupportRepository`. The rest of the code remains the same.