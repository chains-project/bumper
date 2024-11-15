```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = new HashSet<>();
        if (globalConfig.getEnabledLanguages() != null) {
            enabledLanguages.addAll(globalConfig.getEnabledLanguages());
        }
        if (globalConfig.isStandaloneMode()) {
            enabledLanguages.addAll(globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode());
        } else {
            enabledLanguages.addAll(globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInConnectedMode());
        }

        return AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .addEnabledLanguages(enabledLanguages)
                .build();
    }
```