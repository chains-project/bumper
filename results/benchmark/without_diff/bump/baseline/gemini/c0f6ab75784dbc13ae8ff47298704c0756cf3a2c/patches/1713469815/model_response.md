```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider());
        // Check if the configuration requires a specific class loader
        if (globalConfig.getClassLoader() != null) {
            builder.setClassLoader(globalConfig.getClassLoader());
        }
        return builder.build();
    }
```