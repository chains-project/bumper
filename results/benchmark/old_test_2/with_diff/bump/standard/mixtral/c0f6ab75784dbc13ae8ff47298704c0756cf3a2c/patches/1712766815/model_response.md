private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository repo = new LanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(repo.getEnabledLanguagesInConnectedMode())
        .setExtraProperties(repo.getEnabledLanguagesInStandaloneMode())
        .setWorkDir(repo.getWorkDir())
        .setModulesProvider(repo.getModulesProvider())
        .build();
}