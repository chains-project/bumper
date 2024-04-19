```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = new HashSet<>();
        if (globalConfig.getConnectedMode()) {
            enabledLanguages.addAll(globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInConnectedMode());
        } else {
            enabledLanguages.addAll(globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode());
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