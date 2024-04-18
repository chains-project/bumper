Here's a possible patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyVersion(DependencyVersion.getDefaultVersion()) // Add this line
            .build();
}
```
The patch adds the line `setDependencyVersion(DependencyVersion.getDefaultVersion())` to the `buildAnalysisEngineConfiguration()` method. This sets the `DependencyVersion` to the default version, which should resolve the issue of the missing symbol.

It's important to note that this is just one possible solution, and there may be other ways to fix the error. Additionally, this patch assumes that the `DependencyVersion` class is available in the codebase, if not, you may need to add it as a dependency or use a different approach to set the dependency version.