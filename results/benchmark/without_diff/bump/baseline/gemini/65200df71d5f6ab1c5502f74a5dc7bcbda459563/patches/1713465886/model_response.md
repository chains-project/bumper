```java
 private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        // Create a new builder for the AnalysisEngineConfiguration
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();

        // Set the enabled languages from the global configuration
        builder.addEnabledLanguages(globalConfig.getEnabledLanguages());

        // Set the client PID from the global configuration
        builder.setClientPid(globalConfig.getClientPid());

        // Set the extra properties from the global configuration
        builder.setExtraProperties(globalConfig.extraProperties());

        // Set the work directory from the global configuration
        builder.setWorkDir(globalConfig.getWorkDir());

        // Set the modules provider from the global configuration
        builder.setModulesProvider(globalConfig.getModulesProvider());

        // Return the built AnalysisEngineConfiguration
        return builder.build();
    }
```