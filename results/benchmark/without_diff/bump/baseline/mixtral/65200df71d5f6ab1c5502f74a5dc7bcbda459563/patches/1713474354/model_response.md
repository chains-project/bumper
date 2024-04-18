Here's a proposed patch for the failing client code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    DependencyCheckConfiguration dependencyCheckConfig = new DependencyCheckConfiguration();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(dependencyCheckConfig::getModules)
            .build();
}
```

This patch creates a new `DependencyCheckConfiguration` object to replace the use of the removed `getModulesProvider()` method. The `setModulesProvider()` method is then called with a method reference to the `getModules()` method of the new `DependencyCheckConfiguration` object. This should allow the code to compile and run successfully.