```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepository(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode()).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```