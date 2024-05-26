private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = org.sonarsource.sonarlint.core.languages.Languages.get(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalWorkDir.toAbsolutePath().toString())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalWorkDir.toAbsolutePath().toString())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModuleGraph().getTopology().getVertices().stream().map(v -> (org.sonarsource.sonarlint.core.analysis.api.Module) -> new org.sonarsource.sonarlint.core.analysis.opal.DefaultOpalModule(v.key(), v.data())).collect(Collectors.toList()))
        .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
        .build();
}