Here's the updated method with changes to use the new API:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration defaultForkConfiguration = new org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration();
    org.apache.maven.plugin.surefire.booterclient.lazytestprovider.Commandline commandLine = defaultForkConfiguration.createCommandLine(new org.apache.maven.surefire.booter.SurefireBooterFactory.SurefireLauncherConfiguration(), 0, testSrcFolder);
    org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProvider lazyTestProvider = new org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProvider(commandLine);
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, lazyTestProvider.getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The changes include:

1. Creating a `DefaultForkConfiguration` object.
2. Using `createCommandLine` method with the new signature.
3. Creating a `LazyTestProvider` object with the `commandLine`.
4. Using `getTestListResolver` method from `LazyTestProvider` to get the `TestListResolver` instance.
5. Using `getWildcard` method from `TestListResolver` to get the wildcard string.