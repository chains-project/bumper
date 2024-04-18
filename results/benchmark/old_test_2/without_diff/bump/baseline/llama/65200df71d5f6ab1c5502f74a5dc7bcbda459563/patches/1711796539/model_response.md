Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.fromMap(globalConfig.getDependencyVersion()))
            .build();
}
```
The patch adds a new argument `setDependencyVersion(DependencyVersion.fromMap(globalConfig.getDependencyVersion()))` to the `AnalysisEngineConfiguration.builder()` method. This sets the `DependencyVersion` of the `AnalysisEngineConfiguration` to the version specified in the `globalConfig.getDependencyVersion()` map.

This patch addresses the error by providing a valid `DependencyVersion` object to the `AnalysisEngineConfiguration` constructor, which resolves the issue of the missing `DependencyVersion` object.