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
The patch adds a missing `setDependencyVersion()` method call to the `AnalysisEngineConfiguration.builder()` chain. This call sets the `DependencyVersion` for the analysis engine, which is required to resolve the error. The `DependencyVersion` is obtained from the `globalConfig.getDependencyVersions()` method, which returns a map of dependency versions. The `DependencyVersion.fromMap()` method is used to create a `DependencyVersion` object from the map.