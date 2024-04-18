```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setLanguageSupportRepository(new LanguageSupportRepository() {
                    @Override
                    public Set<String> getEnabledLanguagesInConnectedMode() {
                        return super.getEnabledLanguages();
                    }

                    @Override
                    public Set<String> getEnabledLanguagesInStandaloneMode() {
                        return super.getEnabledLanguages();
                    }
                })
                .build();
    }
```
This patch creates a new instance of `LanguageSupportRepository` and overrides the `getEnabledLanguagesInConnectedMode` and `getEnabledLanguagesInStandaloneMode` methods to call the `getEnabledLanguages` method of the superclass. This allows the `AnalysisEngineConfiguration` builder to use the new `LanguageSupportRepository` instance to retrieve the list of enabled languages.