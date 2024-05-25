Here's the proposed patch for the failing method:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    PropertyAccessor propertyAccessor = new PropertyAccessor();
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(propertyAccessor.getEnabledLanguages())
            .setClientPid(propertyAccessor.getClientPid())
            .setExtraProperties(propertyAccessor.extraProperties())
            .setWorkDir(propertyAccessor.getWorkDir())
            .setModulesProvider(propertyAccessor.getModulesProvider())
            .build();
}
```

Assuming `PropertyAccessor` is a new class that you can add to the client code to access the `globalConfig` properties. This new class can use reflection or other means to access the properties from the external dependency.