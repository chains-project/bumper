Here's the proposed patch:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.shared.utils.os.DirectoryScanner directoryScanner = new org.apache.maven.shared.utils.os.DirectoryScanner(testSrcFolder, new org.apache.maven.shared.utils.fn.WildcardPattern());
    return directoryScanner.scan();
}
```

Note that I replaced the `org.apache.maven.plugin.surefire.util.DirectoryScanner` class with `org.apache.maven.shared.utils.os.DirectoryScanner`, and the `TestListResolver.getWildcard()` method with `new WildcardPattern()`. This should fix the "cannot find symbol" error.