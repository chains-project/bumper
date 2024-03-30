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
The proposed patch adds the `setDependencyVersion()` method to the `AnalysisEngineConfiguration.builder()` object, passing in `DependencyVersion.fromMap(globalConfig.getDependencyVersion())` as its argument. This sets the dependency version for the analysis engine configuration, which was previously missing and causing the error.

Note that this patch assumes that `DependencyVersion` is a class provided by the SonarQube API, and that `globalConfig.getDependencyVersion()` returns a map containing the dependency version information. If this is not the case, the patch may need to be modified accordingly.