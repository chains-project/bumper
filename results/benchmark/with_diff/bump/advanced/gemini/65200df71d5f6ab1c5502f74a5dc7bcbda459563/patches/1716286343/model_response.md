```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    java.util.Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    boolean connectedMode = sorald.sonar.SonarLintEngine.globalConfig.isSonarQubeConnected();
    java.util.Set<org.sonarsource.sonarlint.core.commons.Language> languages = connectedMode ? 
        org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInConnectedMode() : 
        org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInStandaloneMode();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(languages).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```