```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    boolean connectedMode = sorald.sonar.SonarLintEngine.globalConfig.isSonarQubeConnected();
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = connectedMode ?
            sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository().getEnabledLanguagesInConnectedMode() :
            sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(enabledLanguages).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```