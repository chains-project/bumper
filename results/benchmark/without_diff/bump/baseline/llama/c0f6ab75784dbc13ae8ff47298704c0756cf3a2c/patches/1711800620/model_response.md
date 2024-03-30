Here's a proposed patch to fix the error:
```diff
- private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
+ private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration(GlobalConfig globalConfig) {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
    }
```
The patch takes the `GlobalConfig` object as a parameter, which is not null, and uses its methods to set the properties of the `AnalysisEngineConfiguration` object. This patch should fix the error by providing the required values for the `AnalysisEngineConfiguration` object.