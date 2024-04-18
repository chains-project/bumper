Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.fromString("1.0")) // Add this line
            .build();
}
```
The error message indicates that the `DependencyVersion` class cannot be found. To fix this, we can add the `setDependencyVersion` method to the `AnalysisEngineConfiguration.builder()` object, which is available in the `org.sonar.api.utils.analysis.DependencyVersion` class.

This change should allow the code to compile and run without any issues related to the `DependencyVersion` class.