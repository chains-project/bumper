```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        LanguageSupportRepository languageSupportRepository = globalConfig.getModulesProvider().getInstance(LanguageSupportRepository.class);
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInStandaloneMode())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```