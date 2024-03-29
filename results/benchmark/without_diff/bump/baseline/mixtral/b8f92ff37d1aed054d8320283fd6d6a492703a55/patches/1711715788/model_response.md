Here's a suggested patch to fix the failing code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    directoryScanner.scan();
    ClassFileSet classFiles = directoryScanner.getClasses();
    return classFiles.getIncludedClasses();
}
```

The patch modifies the code to use `ClassFileSet` instead of the deprecated `getClasses()` method. The `ClassFileSet` class has a `getIncludedClasses()` method that returns the list of included classes. This should resolve the "cannot find symbol" error.