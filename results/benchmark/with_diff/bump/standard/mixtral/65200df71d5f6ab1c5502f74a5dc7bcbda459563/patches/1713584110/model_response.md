Here is a possible patch for the client code:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    org.sonarsource.sonarlint.core.languages.LanguageSupportRepository repository = new org.sonarsource.sonarlint.core.languages.LanguageSupportRepository();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(repository.getEnabledLanguagesInConnectedMode())
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```
The changes I made are:

* I created a new instance of `LanguageSupportRepository` to use its methods for getting the enabled languages.
* I replaced the call to `getEnabledLanguages()` with a call to `getEnabledLanguagesInConnectedMode()`, which is a new method in the updated library version.

I also kept the rest of the code unchanged, as you requested.

Note: I am assuming that the `LanguageSupportRepository` class is available and visible to the client code. If it is not, you may need to import it or adjust the package structure accordingly.