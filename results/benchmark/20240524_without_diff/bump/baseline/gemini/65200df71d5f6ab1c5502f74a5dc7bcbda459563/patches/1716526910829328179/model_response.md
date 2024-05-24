```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages().stream()
                .map(Language::fromCode)
                .collect(Collectors.toSet());

        return AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .addEnabledLanguages(enabledLanguages)
                .build();
    }
```