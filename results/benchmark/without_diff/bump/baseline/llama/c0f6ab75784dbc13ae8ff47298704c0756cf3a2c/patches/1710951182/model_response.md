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
        return Arrays.asList(new LanguageModuleDescriptor("js", "js")); // Add this method
    }
```
The error is caused by the fact that the `AnalysisEngineConfiguration` class has been updated to use the `LanguageModuleDescriptor` class, which is not available in the older version of the `sonar-api` library that the code is using.

To fix the error, we can add a method that returns a list of `LanguageModuleDescriptor` objects, which can be used to set the `languageModuleDescriptors` property of the `AnalysisEngineConfiguration` object.

We can also remove the `Override` annotation, as it is not necessary in this case.

Note that this patch assumes that the `LanguageModuleDescriptor` class is available in the version of the `sonar-api` library that you are using. If this is not the case, you may need to use a different approach to fix the error.