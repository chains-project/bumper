```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    for (org.sonarsource.sonarlint.core.commons.Language language : enabledLanguages) {
        org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Builder builder = org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder();
        builder.addEnabledLanguage(language);
        builder.setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid());
        builder.setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties());
        builder.setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir());
        builder.setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider());
    }
    return builder.build();
}
```