Here's a proposed patch to fix the error:

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

The changes include:

* Replacing `AnalysisEngineConfiguration.builder()` with `new AnalysisEngineConfiguration.Builder()` to create a new instance of the builder.
* Replacing `addEnabledLanguages()` with `setLanguages()` to set the enabled languages.
* Removing the `@Override` annotation from the method. This is safe to do since the method is not overriding any method in the new version.

Note that the changes made in the code are only for fixing the compilation error and the behavior of the method should remain the same.