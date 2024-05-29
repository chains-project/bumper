Here's the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .setOption(new org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Option("sonar.sources", "."))
        .setOption(new org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Option("sonar.test.exclusions", ""))
        .setOption(new org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Option("sonar.language", getLanguageKey(enabledLanguages)))
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}

private static String getLanguageKey(Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages) {
    if (enabledLanguages.size() == 1) {
        return enabledLanguages.iterator().next().getLanguageKey();
    }
    return "java";
}
```

This patch replaces the `addEnabledLanguages` method with the `setOption` method to set the language key based on the enabled languages. It also adds a helper method `getLanguageKey` to get the language key based on the enabled languages. The patch assumes that if there is only one enabled language, the language key for that language should be used; otherwise, the language key should be "java".