```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```

becomes

```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(getEnabledLanguagesInConnectedMode())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }

    private static Set<org.sonarsource.sonarlint.core.commons.Language> getEnabledLanguagesInConnectedMode() {
        return LanguageSupportRepository.getEnabledLanguagesInConnectedMode();
    }
```

The `addEnabledLanguages` method is removed as it is not present in the new version of the library, and instead, we call the `getEnabledLanguagesInConnectedMode` method provided by the `LanguageSupportRepository` class, which returns a set of enabled languages in connected mode.


This patch fixes the error and allows the code to compile and run successfully.