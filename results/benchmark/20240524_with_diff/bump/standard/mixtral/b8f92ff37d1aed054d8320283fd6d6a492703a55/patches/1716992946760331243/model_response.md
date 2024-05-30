Here's the patched method using the new library version:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static org.apache.maven.surefire.api.testset.TestListResolver getTestListResolver() {
    org.apache.maven.plugin.surefire.booterclient.ForkConfiguration forkConfiguration = new org.apache.maven.plugin.surefire.booterclient.JarManifestForkConfiguration();
    return forkConfiguration.createTestListResolver();
}
```

The `getTestListResolver` method is introduced to create an instance of `TestListResolver` using the new `createTestListResolver` method from `ForkConfiguration`. This way, we can access the `getWildcard` method without directly referencing `TestListResolver`.