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
The patch adds a new method `getLanguageModuleDescriptors()` that creates a list of `LanguageModuleDescriptor` objects for the enabled languages. The `setLanguageModuleDescriptors()` method is then called on the `AnalysisEngineConfiguration.builder()` object with this list.

The error message indicates that the `setLanguageModuleDescriptors()` method is not found, which suggests that the `AnalysisEngineConfiguration` class has been updated to require the `LanguageModuleDescriptors` parameter. By adding the `getLanguageModuleDescriptors()` method, we provide the required parameter to the `setLanguageModuleDescriptors()` method, which should fix the error.