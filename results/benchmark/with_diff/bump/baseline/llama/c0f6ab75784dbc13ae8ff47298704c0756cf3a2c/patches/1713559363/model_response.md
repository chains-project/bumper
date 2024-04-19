Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setLanguageSupportRepository(new LanguageSupportRepository() {
                    @Override
                    public Set<Language> getEnabledLanguagesInConnectedMode() {
                        return globalConfig.getEnabledLanguages();
                    }

                    @Override
                    public Set<Language> getEnabledLanguagesInStandaloneMode() {
                        return globalConfig.getEnabledLanguages();
                    }
                })
                .build();
    }
```
The patch creates a new instance of `LanguageSupportRepository` and overrides the `getEnabledLanguagesInConnectedMode` and `getEnabledLanguagesInStandaloneMode` methods to return the `globalConfig.getEnabledLanguages()` value. This allows the `AnalysisEngineConfiguration` builder to use the new methods introduced in the updated library version.