Here's a possible patch to fix the error:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder().addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()).setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid()).setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties()).setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir()).setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider()).setLanguageConfig(new sorald.sonar.SonarLintEngine.LanguageConfig() {
        @Override
        public java.util.Set<org.sonarsource.sonarlint.core.commons.Language> getEnabledLanguages() {
            return sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
        }
    }).build();
}
```
The patch creates a new `LanguageConfig` instance that delegates to the `globalConfig` instance's `getEnabledLanguages()` method to provide the list of enabled languages. This allows the `addEnabledLanguages()` method to be called on the `AnalysisEngineConfiguration.Builder` instance without any issues.