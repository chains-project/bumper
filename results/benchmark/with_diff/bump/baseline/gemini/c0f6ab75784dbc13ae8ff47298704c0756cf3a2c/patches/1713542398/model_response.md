```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    // Get the enabled languages from the global config.
    Set<Language> enabledLanguages = globalConfig.getEnabledLanguages();

    // Create a builder for the AnalysisEngineConfiguration.
    AnalysisEngineConfiguration.Builder builder = AnalysisEngineConfiguration.builder()
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider());

    // Check if the enabled languages set is empty.
    if (enabledLanguages.isEmpty()) {
        // If the enabled languages set is empty, use the default language support repository.
        builder.setLanguageSupportRepository(LanguageSupportRepository.getDefault());
    } else {
        // If the enabled languages set is not empty, use the language support repository that supports the enabled languages.
        builder.setLanguageSupportRepository(LanguageSupportRepository.create(enabledLanguages));
    }

    // Return the built AnalysisEngineConfiguration.
    return builder.build();
}
```