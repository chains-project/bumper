Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setDependencyVersion(DependencyVersion.fromString("2.12.0")) // Add this line
                .build();
    }
```
The `DependencyVersion` class is from the `org.sonar.api.utils.DependencyVersion` package, which is not mentioned in the error message. The `DependencyVersion.fromString("2.12.0")` line sets the dependency version to a known good version, which should resolve the error.