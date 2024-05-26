private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository repo = new LanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setExtraProperties(repo.extraProperties())
        .setWorkDir(repo.getWorkDir())
        .setModulesProvider(repo.getModulesProvider())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .addEnabledLanguages(repo.getEnabledLanguagesInConnectedMode())
        .build();
}