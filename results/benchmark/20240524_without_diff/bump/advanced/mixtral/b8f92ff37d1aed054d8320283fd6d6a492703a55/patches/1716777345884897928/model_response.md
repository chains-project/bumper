Here's a possible patch for the given client code:

```java
import org.apache.maven.shared.utils.StringUtils;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, StringUtils.join(new String[]{"**/*.class"}, StringUtils.FILE_SEPARATOR));
    return directoryScanner.scan().getClasses();
}
```

In this patch, we import the `StringUtils` class from `org.apache.maven.shared.utils` package, which provides the `join` method to replace the deprecated `getWildcard()` method from `org.apache.maven.surefire.api.testset.TestListResolver`.

Note that the `getWildcard()` method has been deprecated since Maven Surefire 2.22.0 and removed in Maven Surefire 3.0.0-M1. The recommended way to specify the wildcard pattern is to use a string array and join it with the file separator.