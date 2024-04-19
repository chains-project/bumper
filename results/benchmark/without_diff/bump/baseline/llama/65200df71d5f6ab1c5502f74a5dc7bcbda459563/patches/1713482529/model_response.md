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
The proposed patch adds the `setDependencyVersion()` method call to the `AnalysisEngineConfiguration.builder()` chain. This call sets the `DependencyVersion` of the `AnalysisEngineConfiguration` to the version specified in the `globalConfig.getDependencyVersions()` map.

The `DependencyVersion` class is a part of the `org.sonar.api.utils.Dependency Versions` class, which is not shown in the provided code snippet. Therefore, it's assumed that the `DependencyVersion` class is available in the project's classpath.

The `setDependencyVersion()` method call fixes the error by providing the correct version of the dependency to the `AnalysisEngineConfiguration` object.