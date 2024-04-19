Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.fromMap(globalConfig.getDependencyVersions()))
            .build();
}
```
The patch adds the `setDependencyVersion()` method to the `AnalysisEngineConfiguration.builder()` object, which is available in the latest version of the library. This method allows you to specify the dependency version for the analysis engine, which should resolve the issue with the missing `DependencyVersion` class.

Note that the `setDependencyVersion()` method takes a `DependencyVersion` object as a parameter, which is created using the `DependencyVersion.fromMap()` method. This method takes a map of dependency names and versions, and returns a `DependencyVersion` object that represents the specified dependencies. In this case, we're passing in the `globalConfig.getDependencyVersions()` map, which should contain the necessary dependency information.