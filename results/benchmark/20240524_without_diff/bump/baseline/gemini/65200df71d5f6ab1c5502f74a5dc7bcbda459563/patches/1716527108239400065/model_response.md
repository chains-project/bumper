```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = globalConfig.getEnabledLanguages();
        if (globalConfig.isStandaloneMode()) {
            return AnalysisEngineConfiguration.builder()
                    .setClientPid(globalConfig.getClientPid())
                    .setExtraProperties(globalConfig.extraProperties())
                    .setWorkDir(globalConfig.getWorkDir())
                    .setModulesProvider(globalConfig.getModulesProvider())
                    .setLanguageSupportRepository(new LanguageSupportRepository(Collections.emptySet(), enabledLanguages))
                    .build();
        } else {
            return AnalysisEngineConfiguration.builder()
                    .setClientPid(globalConfig.getClientPid())
                    .setExtraProperties(globalConfig.extraProperties())
                    .setWorkDir(globalConfig.getWorkDir())
                    .setModulesProvider(globalConfig.getModulesProvider())
                    .setLanguageSupportRepository(new LanguageSupportRepository(enabledLanguages, Collections.emptySet()))
                    .build();
        }
    }
```