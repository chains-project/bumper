Here's a proposed patch to fix the error:
```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setLanguageModuleDescriptors(getLanguageModuleDescriptors()) // Add this line
                .build();
    }

    private static List<LanguageModuleDescriptor> getLanguageModuleDescriptors() {
        return Arrays.asList(new LanguageModuleDescriptor[] {
                new JavaLanguageModuleDescriptor(),
                new PythonLanguageModuleDescriptor(),
                new CSharpLanguageModuleDescriptor(),
                new JavaScriptLanguageModuleDescriptor(),
                new TypeScriptLanguageModuleDescriptor()
        });
    }
```
The `getLanguageModuleDescriptors()` method is created to provide the list of language module descriptors. The `LanguageModuleDescriptor` class is part of the `org.sonar.api.utils` package, which is a dependency of the `sonar-api` module.

The `setLanguageModuleDescriptors()` method is called on the `AnalysisEngineConfiguration.builder()` object, passing the list of language module descriptors returned by `getLanguageModuleDescriptors()`.

This patch fixes the error by providing the list of language module descriptors required by the `AnalysisEngineConfiguration` constructor.