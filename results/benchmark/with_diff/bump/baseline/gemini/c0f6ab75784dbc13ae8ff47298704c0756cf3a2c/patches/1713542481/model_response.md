```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder()
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
        if (enabledLanguages != null) {
            builder.setEnabledLanguages(enabledLanguages);
        }
        return builder.build();
    }
```