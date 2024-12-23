```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = new HashSet<>();
        if (globalConfig.isStandaloneMode()) {
            enabledLanguages.addAll(globalConfig.getModulesProvider().getModules().stream()
                    .flatMap(module -> module.getLanguages().stream())
                    .collect(Collectors.toSet()));
        } else {
            enabledLanguages.addAll(globalConfig.getModulesProvider().getModules().stream()
                    .flatMap(module -> module.getLanguages().stream())
                    .filter(language -> globalConfig.getEnabledLanguages().contains(language.getName()))
                    .collect(Collectors.toSet()));
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