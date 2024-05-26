```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Builder builder = org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder();
    builder.setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid());
    builder.setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties());
    builder.setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir());
    builder.setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider());
    if (sorald.sonar.SonarLintEngine.globalConfig.getConnectedMode()) {
        builder.addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository().getEnabledLanguagesInConnectedMode());
    } else {
        builder.addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode());
    }
    return builder.build();
}
```