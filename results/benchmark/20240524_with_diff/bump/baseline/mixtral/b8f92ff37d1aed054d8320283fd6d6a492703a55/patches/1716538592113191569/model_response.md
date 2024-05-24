Here's the fixed `getTestListResolver` method:

```java
private TestListResolver getTestListResolver() {
    return new TestListResolver(new DefaultSurefireForkFactory(), new ClasspathExplorer(), new RunOrder(), new ConfigurationParameters());
}
```

I added the required constructor arguments for `TestListResolver` based on the available constructors in the new library version. These arguments are:

1. `DefaultSurefireForkFactory`: A class for creating forks for test execution.
2. `ClasspathExplorer`: A class for exploring the classpath.
3. `RunOrder`: A class for specifying the order in which tests should be run.
4. `ConfigurationParameters`: A class for storing configuration parameters.

These classes are available in the new library version, so the code should compile and run without issues.