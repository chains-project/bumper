Here is a patched version of the failing method that should resolve the error:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration defaultForkConfiguration = new org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration();
    org.apache.maven.plugin.surefire.booterclient.lazytestprovider.Commandline commandLine = defaultForkConfiguration.createCommandLine(new org.apache.maven.surefire.booter.SurefireBooterFactory.SurefireBooterConfiguration(), 0, testSrcFolder);
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, commandLine);
    return directoryScanner.scan().getClasses();
}
```

The patch creates a `Commandline` object through the new `createCommandLine` method added to `DefaultForkConfiguration`. This object is then passed to the `DirectoryScanner` constructor.

Note that the `TestListResolver` class is no longer used, as it seems to have been removed from the new version of the library.