Here is a possible patch for the code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    directoryScanner.scan();
    ClassFileSet classFiles = directoryScanner.getClasses();
    return classFiles.getFiles();
}
```

This patch uses the `getFiles()` method of the `ClassFileSet` class to get the list of classes. This method was added in a newer version of the library, so it should be available in the version that the code is using.

Note that this patch assumes that the `DirectoryScanner` class and the `TestListResolver` class are still available and unchanged in the new version of the library. If these classes have been removed or modified, then this patch may not work. In that case, you may need to find a different solution.