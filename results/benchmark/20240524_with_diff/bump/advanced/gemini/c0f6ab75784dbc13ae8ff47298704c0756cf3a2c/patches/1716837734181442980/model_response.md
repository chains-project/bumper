```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    boolean connectedMode = sorald.sonar.SonarLintEngine.globalConfig.isSonarQubeConnected();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(connectedMode ? sorald.sonar.SonarLintEngine.globalConfig.getLanguagesSupportRepository().getEnabledLanguagesInConnectedMode() : sorald.sonar.SonarLintEngine.globalConfig.getLanguagesSupportRepository().getEnabledLanguagesInStandaloneMode()).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```