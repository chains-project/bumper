```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    List<org.sonarsource.sonarlint.core.commons.Language> languageList = new ArrayList<>(enabledLanguages);
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguage(languageList.toArray(new org.sonarsource.sonarlint.core.commons.Language[0])).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```