Here's the patched method using the new library version:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static org.apache.maven.surefire.api.testset.TestListResolver getTestListResolver() {
    org.apache.maven.plugin.surefire.booterclient.ForkConfiguration forkConfig = new org.apache.maven.plugin.surefire.booterclient.ClasspathForkConfiguration();
    return forkConfig.createTestListResolver();
}
```

The main changes are:

1. A new private method `getTestListResolver()` has been added to create and configure a `TestListResolver` instance using the new `createTestListResolver()` method from the `ForkConfiguration` class.
2. The `DirectoryScanner` constructor now uses the `TestListResolver` instance returned by `getTestListResolver()`.