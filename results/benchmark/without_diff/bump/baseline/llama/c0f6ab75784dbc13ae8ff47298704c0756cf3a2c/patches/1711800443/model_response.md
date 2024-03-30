Here's a proposed patch to fix the error:
```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    return AnalysisEngineConfiguration.builder()
            .addEnabledLanguages(globalConfig.getEnabledLanguages())
            .setClientPid(globalConfig.getClientPid())
            .setExtraProperties(globalConfig.extraProperties())
            .setWorkDir(globalConfig.getWorkDir())
            .setModulesProvider(globalConfig.getModulesProvider())
            .setDependencyProvider(new DefaultDependencyProvider(
                    Arrays.asList(new Module[]{
                            new Module("org.sonar.squid.SonarPlugin"),
                            new Module("org.sonar.squid.SonarPlugin"),
                            new Module("org.sonar.squid.SonarPlugin")
                    })
            )
            .build();
}
```
The error was caused by the missing `DependencyProvider` in the `AnalysisEngineConfiguration` builder. By adding a `DependencyProvider` with the necessary modules, the error should be resolved.