```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Builder builder = org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder();
    if (sorald.sonar.SonarLintEngine.globalConfig.isStandaloneMode()) {
        builder.addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInStandaloneMode());
    } else {
        builder.addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider().getLanguageSupportRepository().getEnabledLanguagesInConnectedMode());
    }
    builder.setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
            .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
            .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir());
    return builder.build();
}
```