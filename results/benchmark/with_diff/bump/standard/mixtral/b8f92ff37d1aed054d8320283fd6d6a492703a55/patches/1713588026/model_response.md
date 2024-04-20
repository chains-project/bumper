Here's the proposed patch for the given client code:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

In this patch, I have replaced the static method call `TestListResolver.getWildcard()` with an instance method call `new TestListResolver().getWildcard()`. This is because the `getWildcard()` method is no longer a static method in the new library version.