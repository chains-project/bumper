```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepository();
    java.util.Set enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    if (sorald.sonar.SonarLintEngine.globalConfig.isInConnectedMode()) {
        enabledLanguages = languageSupportRepository.getEnabledLanguagesInConnectedMode();
    } else {
        enabledLanguages = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
    }
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```