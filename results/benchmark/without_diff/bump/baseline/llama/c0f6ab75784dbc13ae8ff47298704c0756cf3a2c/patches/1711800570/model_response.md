Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyAnalyzer(new DependencyAnalyzer(globalConfig.getDependencyAnalyzer()))
            .build();
}
```
The proposed patch adds a new `setDependencyAnalyzer` method call to the `AnalysisEngineConfiguration.builder()` method chain. This call sets the `DependencyAnalyzer` instance to the same instance that is passed to the `globalConfig.getDependencyAnalyzer()` method.

This patch addresses the "cannot find symbol" error by providing a valid `DependencyAnalyzer` instance to the `AnalysisEngineConfiguration` constructor. The `DependencyAnalyzer` instance is now being set using the `setDependencyAnalyzer` method, which should resolve the error.