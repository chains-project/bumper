```
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setLanguageSupportRepository(new LanguageSupportRepository(globalConfig.getLanguages()))
                .build();
    }
```

The change is using the `LanguageSupportRepository` constructor that takes a list of languages instead of the removed `addEnabledLanguages` method.