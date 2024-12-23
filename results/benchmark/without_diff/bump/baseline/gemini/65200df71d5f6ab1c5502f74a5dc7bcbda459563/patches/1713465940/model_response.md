```java
  private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        // Create a new builder for the AnalysisEngineConfiguration
        AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder();

        // Add the enabled languages to the builder
        builder.addEnabledLanguages(globalConfig.getEnabledLanguages());

        // Set the client PID to the builder
        builder.setClientPid(globalConfig.getClientPid());

        // Set the extra properties to the builder
        builder.setExtraProperties(globalConfig.extraProperties());

        // Set the work directory to the builder
        builder.setWorkDir(globalConfig.getWorkDir());

        // Set the modules provider to the builder
        builder.setModulesProvider(globalConfig.getModulesProvider());

        // Build and return the AnalysisEngineConfiguration
        return builder.build();
    }
```