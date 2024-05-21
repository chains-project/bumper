Here's the fixed version of the failing method using the new library version:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The change here is creating a new instance of `TestListResolver` and then calling the `getWildcard()` method on that instance.