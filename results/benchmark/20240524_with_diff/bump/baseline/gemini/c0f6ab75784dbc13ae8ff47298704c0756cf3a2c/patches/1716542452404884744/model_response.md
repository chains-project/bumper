```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = new HashSet<>();
        if (globalConfig.getEnabledLanguages() != null) {
            enabledLanguages.addAll(globalConfig.getEnabledLanguages());
        }
        if (globalConfig.getWorkDir() != null) {
            enabledLanguages.addAll(LanguageSupportRepository.getEnabledLanguagesInStandaloneMode(globalConfig.getWorkDir()));
        }
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(enabledLanguages)
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```