Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setLanguageVersion(LanguageVersion.of(JavaVersion.VERSION_1_8)) // Add this line
            .build();
}
```
The error message indicates that the `LanguageVersion` enum cannot be found. To fix this, we can add the `setLanguageVersion()` method to the `AnalysisEngineConfiguration.builder()` chain. This method sets the language version to Java 8, which is compatible with the `LanguageVersion` enum.

By adding this line, we ensure that the `LanguageVersion` enum is available when building the `AnalysisEngineConfiguration`.