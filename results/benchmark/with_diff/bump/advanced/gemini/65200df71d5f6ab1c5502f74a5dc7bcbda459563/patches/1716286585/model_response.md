```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    java.util.Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    boolean isConnectedMode = sorald.sonar.SonarLintEngine.globalConfig.isConnectedMode();
    java.util.Set<org.sonarsource.sonarlint.core.commons.Language> languages;
    if (isConnectedMode) {
        languages = org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInConnectedMode();
    } else {
        languages = org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInStandaloneMode();
    }
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(languages).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```