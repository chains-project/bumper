Here's a proposed patch to fix the error:
```
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
The proposed patch adds the `setDependencyVersion()` method to the `AnalysisEngineConfiguration.builder()` object, passing in the `DependencyVersion.fromMap()` method that takes a map of dependency versions as an argument. This should fix the error by providing the required `DependencyVersion` object to the `AnalysisEngineConfiguration` builder.