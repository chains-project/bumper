```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Builder builder = org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder();
    builder.setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid());
    builder.setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties());
    builder.setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir());
    builder.setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider());
    // Use the added method setLanguages to set the enabled languages
    builder.setLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages());
    return builder.build();
}
```