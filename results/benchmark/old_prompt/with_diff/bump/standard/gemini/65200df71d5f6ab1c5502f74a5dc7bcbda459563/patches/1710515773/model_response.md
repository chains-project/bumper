```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository();
    java.util.Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = new java.util.HashSet<>();
    enabledLanguages.addAll(languageSupportRepository.getEnabledLanguagesInConnectedMode());
    enabledLanguages.addAll(languageSupportRepository.getEnabledLanguagesInStandaloneMode());
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(enabledLanguages).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```