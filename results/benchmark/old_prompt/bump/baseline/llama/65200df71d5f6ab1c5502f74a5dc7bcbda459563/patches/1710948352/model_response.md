Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setLanguageModuleDescriptors(getLanguageModuleDescriptors()) // ADDED
            .build();
}

private static List<LanguageModuleDescriptor> getLanguageModuleDescriptors() {
    List<LanguageModuleDescriptor> descriptors = new ArrayList<>();
    for (String language : globalConfig.getEnabledLanguages()) {
        descriptors.add(LanguageModuleDescriptor.forLanguage(language)); // ADDED
    }
    return descriptors;
}
```
The error is caused by the fact that the `AnalysisEngineConfiguration` builder doesn't have a `setLanguageModuleDescriptors` method. This patch adds a new method `getLanguageModuleDescriptors` that creates a list of `LanguageModuleDescriptor` objects from the enabled languages and returns it. The `setLanguageModuleDescriptors` method is then called in the `buildAnalysisEngineConfiguration` method with the list of descriptors as its argument.

With this patch, the code should now compile without any errors.