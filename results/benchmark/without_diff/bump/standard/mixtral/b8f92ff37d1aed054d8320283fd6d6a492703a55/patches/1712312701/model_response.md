Here is a potential patch for the issue:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.shared.utils.fn.FileUtils fileUtils = new org.apache.maven.shared.utils.fn.FileUtils();
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, fileUtils.wildcard(fileUtils.fileNamesToMatch("**/*.class")));
    return directoryScanner.scan().getClasses();
}
```

This patch uses the `wildcard` method from `org.apache.maven.shared.utils.fn.FileUtils` instead of `getWildcard` from `org.apache.maven.surefire.api.testset.TestListResolver`. This should resolve the "cannot find symbol" error.