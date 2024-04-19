Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.create(JavaVersion.VERSION_1_8, "1.8"))
            .build();
}
```
The patch adds the `setDependencyVersion()` method to the `AnalysisEngineConfiguration.builder()` object, which fixes the error by specifying the correct version of the Java dependency.