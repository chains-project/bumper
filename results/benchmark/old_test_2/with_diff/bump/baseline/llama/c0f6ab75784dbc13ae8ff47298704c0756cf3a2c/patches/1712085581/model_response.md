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

Replace with:
```
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {ising enabledLanguages = globalConfig.getEnabledLanguages();
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguages)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```
The change is that the `enabledLanguages` variable is created using `globalConfig.getEnabledLanguages()`, and then passed to the `addEnabledLanguages()` method.

This patch removes the need to call `getEnabledLanguages()` on `AnalysisEngineConfiguration.Builder`, which is not available in the new version of the library. Instead, we use the `getEnabledLanguages()` method on `globalConfig`, which is available in both the old and new versions of the library.