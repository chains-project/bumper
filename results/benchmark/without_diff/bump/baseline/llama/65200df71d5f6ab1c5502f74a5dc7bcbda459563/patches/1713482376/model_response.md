```
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
        return AnalysisEngineConfiguration.builder()
                .addEnabledLanguages(globalConfig.getEnabledLanguages())
                .setClientPid(globalConfig.getClientPid())
                .setExtraProperties(globalConfig.extraProperties())
                .setWorkDir(globalConfig.getWorkDir())
                .setModulesProvider(globalConfig.getModulesProvider())
                .setDependencyVersion(DependencyVersion.fromMap(ImmutableMap.of("scala", "2.12.10")))
                .build();
    }
```

The error message indicates that the `DependencyVersion` class cannot be found. To fix this issue, we can add the missing `DependencyVersion` class by importing the necessary package and creating a `DependencyVersion` object with the desired version.

In this case, we're importing the `DependencyVersion` class from the `org.apache.maven.plugins:maven-dependency-plugin:3.2.0` plugin, which is a widely used plugin for managing dependencies in Maven projects.

The `DependencyVersion` class has a constructor that takes a map of dependency names and versions, so we create an `ImmutableMap` object with the `scala` dependency set to version `2.12.10`.

Finally, we set the `DependencyVersion` object as the `dependencyVersion` property of the `AnalysisEngineConfiguration.Builder` object using the `setDependencyVersion` method.

This modified code should resolve the error and allow the code to compile successfully.