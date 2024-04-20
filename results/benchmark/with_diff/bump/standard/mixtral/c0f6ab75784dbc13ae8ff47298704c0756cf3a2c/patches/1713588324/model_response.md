Here's a proposed patch for the client code to fix the error:
```java
import org.sonarsource.sonarlint.core.languages.LanguageSupportRepository;

private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    LanguageSupportRepository languageSupportRepository = new LanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(languageSupportRepository.getEnabledLanguagesInConnectedMode())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```
In this patch, we create a new instance of `LanguageSupportRepository` and use its `getEnabledLanguagesInConnectedMode()` method instead of `getEnabledLanguages()` on `AnalysisEngineConfiguration.Builder`. This should fix the error as the new library version has removed the `getEnabledLanguages()` method.