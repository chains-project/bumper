Here's a possible patch to fix the error:
```java
private static org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages().stream().map(language -> language.name()).collect(Collectors.joining(",")))
            .setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid())
            .setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties())
            .setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir())
            .setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider())
            .build();
}
```
The changes made to the code are:

* Replaced `addEnabledLanguages(Set<Language> enabledLanguages)` with `addEnabledLanguages(Stream<Language> enabledLanguages.stream().map(language -> language.name()).collect(Collectors.joining(",")))` to adapt to the changed signature of the method in the updated dependency.
* Removed the type parameter `java.util.Set<org.sonarsource.sonarlint.core.commons.Language>` from the method call, as it is not necessary with the updated signature.

This patch should fix the error and allow the code to compile again.