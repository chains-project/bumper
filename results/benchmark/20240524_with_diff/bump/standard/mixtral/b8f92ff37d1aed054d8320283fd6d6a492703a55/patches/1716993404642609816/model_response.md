Here's the patched method using the new library version:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static org.apache.maven.surefire.api.testset.TestListResolver getTestListResolver() {
    org.apache.maven.plugin.surefire.booterclient.ForkConfiguration forkConfig = new org.apache.maven.plugin.surefire.booterclient.JarManifestForkConfiguration();
    return forkConfig.createTestListResolver();
}
```

The main change is the introduction of the `getTestListResolver()` method that creates a new `TestListResolver` instance using the `createTestListResolver()` method from the `ForkConfiguration` class. This is needed because the `getWildcard()` method is no longer directly accessible from `TestListResolver`.