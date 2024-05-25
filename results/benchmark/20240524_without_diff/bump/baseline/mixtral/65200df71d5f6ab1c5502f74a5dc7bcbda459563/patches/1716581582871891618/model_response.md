Here's a proposed patch for the failing client code:

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

In this patch, we introduce a new `PropertyAccessor` class that retrieves the necessary properties. This allows us to avoid directly referencing the `globalConfig` object, which may have been removed or renamed in the updated dependency.

Assuming that the `PropertyAccessor` class has the following methods:

```java
public class PropertyAccessor {
    public List<Language> getEnabledLanguages() { ... }
    public int getClientPid() { ... }
    public Properties extraProperties() { ... }
    public File getWorkDir() { ... }
    public ModulesProvider getModulesProvider() { ... }
}
```

This patch should resolve the "cannot find symbol" error.