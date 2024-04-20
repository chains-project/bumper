Here is the proposed patch:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The change is to create a new instance of `TestListResolver` and then call the `getWildcard()` method on that instance. This is necessary because the `getWildcard()` method is no longer a static method in the new version of the library.