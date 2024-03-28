Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setLanguageModuleDescriptors(getLanguageModuleDescriptors()) // Added this line
            .build();
}

private static List<LanguageModuleDescriptor> getLanguageModuleDescriptors() {
    List<LanguageModuleDescriptor> descriptors = new ArrayList<>();
    for (Language language : globalConfig.getEnabledLanguages()) {
        descriptors.add(LanguageModuleDescriptor.forLanguage(language));
    }
    return descriptors;
}
```
The error is caused by the fact that the `AnalysisEngineConfiguration` constructor expects a `List<LanguageModuleDescriptor>` as its last argument, but the `globalConfig.getModulesProvider()` method returns a `ModulesProvider` object, which does not match the expected type.

To fix this issue, we can create a new method called `getLanguageModuleDescriptors()` that converts the `ModulesProvider` object to a list of `LanguageModuleDescriptor` objects, and pass this list to the `AnalysisEngineConfiguration` constructor.

The `getLanguageModuleDescriptors()` method iterates over the enabled languages and creates a `LanguageModuleDescriptor` object for each one, then returns a list of these descriptors.

With this change, the code should now compile and run without any issues.