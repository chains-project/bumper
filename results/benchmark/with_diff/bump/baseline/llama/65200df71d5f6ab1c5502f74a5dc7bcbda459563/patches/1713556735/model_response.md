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

Change the line
```
.addEnabledLanguages(globalConfig.getEnabledLanguages())
```
to
```
.addEnabledLanguages(LanguageSupportRepository.getEnabledLanguagesInConnectedMode())
```
This change uses the new `LanguageSupportRepository` class to retrieve the list of enabled languages, which is now the recommended way to get the list of enabled languages. This should fix the error and allow the code to compile.