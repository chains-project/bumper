```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        if (globalConfig.isStandaloneMode()) {
            return AnalysisEngineConfiguration.builder()
                    .setClientPid(globalConfig.getClientPid())
                    .setExtraProperties(globalConfig.extraProperties())
                    .setWorkDir(globalConfig.getWorkDir())
                    .setModulesProvider(globalConfig.getModulesProvider())
                    .addEnabledLanguages(LanguageSupportRepository.getEnabledLanguagesInStandaloneMode())
                    .build();
        } else {
            return AnalysisEngineConfiguration.builder()
                    .setClientPid(globalConfig.getClientPid())
                    .setExtraProperties(globalConfig.extraProperties())
                    .setWorkDir(globalConfig.getWorkDir())
                    .setModulesProvider(globalConfig.getModulesProvider())
                    .addEnabledLanguages(LanguageSupportRepository.getEnabledLanguagesInConnectedMode())
                    .build();
        }
    }
```