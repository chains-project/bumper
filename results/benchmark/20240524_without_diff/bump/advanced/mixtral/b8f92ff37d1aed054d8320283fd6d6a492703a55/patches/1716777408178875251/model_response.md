Here is the proposed patch:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The failure is caused by the fact that `TestListResolver.getWildcard()` is not a static method, so it cannot be called directly from the class. To fix the issue, I created a new instance of `TestListResolver` and called `getWildcard()` on that instance.