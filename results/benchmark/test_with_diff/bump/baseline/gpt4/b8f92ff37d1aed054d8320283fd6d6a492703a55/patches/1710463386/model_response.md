Based on the error message and the changes in the new library version, the method `getWildcard()` from `TestListResolver` class is no longer available. The library changes do not provide an alternative method to replace `getWildcard()`. Therefore, a possible solution is to manually replace the wildcard functionality.

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, "*");
    return directoryScanner.scan().getClasses();
}
```
In this patch, I replaced `TestListResolver.getWildcard()` with a string `"*"`, which is a common wildcard character that matches any file or directory. This is a common workaround when the method to get a wildcard is not available. However, please ensure this solution fits into your context.