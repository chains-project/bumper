Here's the proposed patch:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

In this patch, I created a new instance of `TestListResolver` and called the `getWildcard()` method on it, instead of calling it statically. This is because the `getWildcard()` method is an instance method of `TestListResolver`, not a static method.