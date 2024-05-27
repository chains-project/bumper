```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    java.util.Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = null;
    if (sorald.sonar.SonarLintEngine.globalConfig.isStandaloneMode()) {
        enabledLanguages = org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInStandaloneMode();
    } else {
        enabledLanguages = org.sonarsource.sonarlint.core.languages.LanguageSupportRepository.getEnabledLanguagesInConnectedMode();
    }
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(enabledLanguages).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```