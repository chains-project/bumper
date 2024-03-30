Here's a proposed patch to fix the error:
```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setDependencyVersion(DependencyVersion.fromString("3.28.0"))
                .build();
    }
```
The error was caused by an external dependency, specifically the `DependencyVersion` class. To fix the error, we added the `setDependencyVersion` method to the `AnalysisEngineConfiguration.builder()` object, and passed it a `DependencyVersion` object with the version string "3.28.0". This version string matches the version of the `DependencyVersion` class that is available in the project's dependencies.