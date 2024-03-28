Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.fromString("2.14.0")) // Add this line
            .build();
}
```
The issue is caused by a missing `DependencyVersion` parameter in the `AnalysisEngineConfiguration.builder()` method call. Adding the `setDependencyVersion()` method call with a hardcoded version string of `"2.14.0"` should resolve the issue.