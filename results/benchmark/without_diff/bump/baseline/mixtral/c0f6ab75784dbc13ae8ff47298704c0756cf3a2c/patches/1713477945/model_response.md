Here's a patch that you can apply to the `buildAnalysisEngineConfiguration()` method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    PropertyNexus globalConfig = new PropertyNexus(); // create a mock PropertyNexus object
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig::getModulesProvider) // use a method reference instead
            .build();
}
```

In this patch, I created a mock `PropertyNexus` object since it's not provided in the code snippet. This should allow the method to compile and run without throwing the "cannot find symbol" error.

Additionally, I changed the `setModulesProvider` line to use a method reference instead of a lambda expression. This is because lambda expressions were introduced in Java 8, and if the external dependency only supports Java 7 or earlier, it might not recognize lambda expressions.

Note that this patch assumes that the `PropertyNexus` class and its methods are still available in the client code, and that the issue is caused by a missing external dependency. If this is not the case, the actual solution might be different.