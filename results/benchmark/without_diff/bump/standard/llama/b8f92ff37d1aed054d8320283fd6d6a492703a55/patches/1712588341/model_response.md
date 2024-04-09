Here's a possible patch to fix the error:
```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, org.apache.maven.surefire.api.testset.TestListResolver.getTestClasses());
    return directoryScanner.scan().getClasses();
}
```
The patch replaces the call to `getWildcard()` with `getTestClasses()`, which is a method added in the same version of the Surefire plugin that introduced the `getWildcard()` method. `getTestClasses()` returns a list of test classes, just like `getWildcard()`, but it does not have the same restriction on the class name pattern.

Note that this patch assumes that you are using the Surefire plugin version 2.22.0 or later, which is the version that introduced the `getTestClasses()` method. If you are using an earlier version of the plugin, you may need to use a different patch.