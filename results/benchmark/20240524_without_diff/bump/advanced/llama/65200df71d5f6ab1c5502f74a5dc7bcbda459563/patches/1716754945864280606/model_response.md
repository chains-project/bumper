```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    List<String> languages = new ArrayList<>();
    for (org.sonarsource.sonarlint.core.commons.Language language : enabledLanguages) {
        languages.add(language.getKey());
    }
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(languages).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).build();
}
```