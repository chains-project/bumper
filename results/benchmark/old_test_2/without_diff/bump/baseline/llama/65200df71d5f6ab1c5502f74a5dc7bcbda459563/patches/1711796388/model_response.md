Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setDependencyVersion(DependencyVersion.fromString("1.11")) // Add this line
                .build();
    }
```
The patch adds the line `.setDependencyVersion(DependencyVersion.fromString("1.11"))` to the `buildAnalysisEngineConfiguration()` method. This sets the dependency version to a specific version, which should resolve the error caused by the external dependency.