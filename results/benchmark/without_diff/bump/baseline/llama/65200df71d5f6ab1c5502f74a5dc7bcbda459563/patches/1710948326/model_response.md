Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setLanguageModuleDescriptors(getLanguageModuleDescriptors()) // added this line
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
The issue is caused by the fact that the `AnalysisEngineConfiguration` builder is trying to access the `LanguageModuleDescriptors` field, which is not available in the version of the library being used. To fix this, we can add a method that creates a list of `LanguageModuleDescriptor` objects for the enabled languages and pass it to the builder.

Note that I've also removed the `Override` annotation, as it's not needed in this case.