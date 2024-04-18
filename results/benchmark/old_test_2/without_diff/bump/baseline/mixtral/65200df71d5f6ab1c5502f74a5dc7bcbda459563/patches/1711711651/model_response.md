Here is a proposed patch for the failing code:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return new AnalysisEngineConfiguration.Builder()
                .setLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .build();
}
```

I noticed that the method `addEnabledLanguages` was replaced by `setLanguages` in the new version of the library. I also added the `new` keyword when creating the `Builder` object, as it is required in some cases.