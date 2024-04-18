Here's a proposed patch to fix the error:
```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setDependencyVersion(DependencyVersion.fromMap(globalConfig.getDependencyVersion())) // Add this line
                .build();
    }
```
The `setDependencyVersion()` method is added to specify the version of the dependency, which is obtained from the `globalConfig.getDependencyVersion()` method. This should resolve the error message and allow the code to compile successfully.