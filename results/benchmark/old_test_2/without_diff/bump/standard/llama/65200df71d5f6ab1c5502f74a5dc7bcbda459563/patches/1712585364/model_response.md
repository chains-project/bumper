Here's a possible patch to fix the error:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream()
                    .map(language -> org.sonarsource.sonarlint.core.commons.Language.valueOf(language.name()))
                    .collect(Collectors.toSet()))
            .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
            .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
            .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
            .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
            .build();
}
```
The change is in the `addEnabledLanguages` method, which now uses a stream to convert the `Set<String>` of language codes to a `Set<org.sonarsource.sonarlint.core.commons.Language>`. This is necessary because the `addEnabledLanguages` method expects a `Set<org.sonarsource.sonarlint.core.commons.Language>` as its argument, but the `getEnabledLanguages` method returns a `Set<String>`.

By using the `stream()` method, we can convert the `Set<String>` to a `Set<org.sonarsource.sonarlint.core.commons.Language>` and pass it to the `addEnabledLanguages` method.

This patch should fix the error and allow the code to compile successfully.