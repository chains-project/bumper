```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    boolean isConnectedMode = sorald.sonar.SonarLintEngine.globalConfig.isConnectedMode();
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = isConnectedMode ?
            org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInConnectedMode() :
            org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInStandaloneMode();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(enabledLanguages).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```