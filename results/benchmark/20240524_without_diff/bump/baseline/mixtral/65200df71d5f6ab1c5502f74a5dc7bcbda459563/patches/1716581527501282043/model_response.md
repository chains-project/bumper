Here's a fixed version of the method that should resolve the issue:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    DependencyCheckConfiguration dependencyCheckConfiguration = globalConfig.getDependencyCheckConfiguration();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyCheckConfiguration(dependencyCheckConfiguration) // Add this line
            .build();
}
```

This patch adds a new line to set the `DependencyCheckConfiguration` object, which was likely removed in the updated version of the external dependency. This assumes that the `globalConfig` object has a getter method for `DependencyCheckConfiguration`. If not, you may need to modify the code accordingly.