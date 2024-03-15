```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository languageSupportRepository = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepository();
    java.util.Set enabledLanguages = languageSupportRepository.getEnabledLanguagesInStandaloneMode();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
            .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
            .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
            .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
            .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
            .build();
}
```
In this patch, I've removed the call to the now non-existent method 'addEnabledLanguages' and replaced it with a new instance of 'LanguageSupportRepository'. Then, I've used its method 'getEnabledLanguagesInStandaloneMode' to get the set of enabled languages. The rest of the code remains the same.