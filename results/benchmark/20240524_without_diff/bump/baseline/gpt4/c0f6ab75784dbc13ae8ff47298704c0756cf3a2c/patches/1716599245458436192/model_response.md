```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();
        if (globalConfig.getEnabledLanguages() != null) {
            builder.addEnabledLanguages(globalConfig.getEnabledLanguages());
        }
        if (globalConfig.getClientPid() != null) {
            builder.setClientPid(globalConfig.getClientPid());
        }
        if (globalConfig.extraProperties() != null) {
            builder.setExtraProperties(globalConfig.extraProperties());
        }
        if (globalConfig.getWorkDir() != null) {
            builder.setWorkDir(globalConfig.getWorkDir());
        }
        if (globalConfig.getModulesProvider() != null) {
            builder.setModulesProvider(globalConfig.getModulesProvider());
        }
        return builder.build();
    }
```