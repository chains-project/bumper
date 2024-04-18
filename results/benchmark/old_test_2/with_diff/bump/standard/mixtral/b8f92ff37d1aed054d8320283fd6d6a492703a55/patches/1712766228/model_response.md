Here's the updated method to fix the error:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The issue was caused by the static method `getWildcard()` being called directly on the class `TestListResolver`. Instead, we need to create an instance of `TestListResolver` and then call the `getWildcard()` method on that instance.