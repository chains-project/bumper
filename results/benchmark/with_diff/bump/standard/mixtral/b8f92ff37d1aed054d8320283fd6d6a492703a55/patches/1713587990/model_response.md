Here's the updated method with the changes to fix the error:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration defaultForkConfiguration = new org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration();
    org.apache.maven.plugin.surefire.booterclient.lazytestprovider.Commandline commandLine = defaultForkConfiguration.createCommandLine(new org.apache.maven.surefire.booter.SurefireBooterFactory().createStartupConfiguration(), 0, testSrcFolder);
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, commandLine);
    return directoryScanner.scan().getClasses();
}
```

The changes include:

1. Replacing the `org.apache.maven.plugin.surefire.util.DirectoryScanner` constructor with the one that accepts a `Commandline` object instead of a `String`.
2. Creating an instance of `org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration` and using its `createCommandLine` method to generate the `Commandline` object for the `DirectoryScanner` constructor.

This solution should resolve the "cannot find symbol" error caused by the removal of the `getWildcard()` method from `org.apache.maven.surefire.api.testset.TestListResolver`.