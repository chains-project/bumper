Here's the proposed patch:

```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Set<org.sonarsource.sonarlint.core.commons.Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
        .addEnabledLanguages(enabledLanguages)
        .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
        .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
        .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
        .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
        .build();
}
```

The patch creates a local variable `enabledLanguages` to store the result of `sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages()`. This allows the method to be called only once, making the code easier to read and potentially improving performance.

The patch then passes `enabledLanguages` to the `addEnabledLanguages` method, which should resolve the "cannot find symbol" error.

Note that the patch does not change the function signature, and does not use any removed library methods. It only adds a local variable and modifies the argument passed to `addEnabledLanguages`.