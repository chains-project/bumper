Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.VERSION_12) // Add this line
            .build();
}
```
The `setDependencyVersion()` method is added to the `AnalysisEngineConfiguration.builder()` object, setting the `DependencyVersion` to `VERSION_12`. This should address the issue of the failing code by specifying a compatible version of the dependency.