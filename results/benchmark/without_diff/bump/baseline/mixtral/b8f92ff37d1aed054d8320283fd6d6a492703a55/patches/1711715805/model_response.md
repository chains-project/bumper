Here's a possible patch to fix the issue:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    directoryScanner.scan();
    ClassFileSet classFiles = directoryScanner.getClasses();
    return classFiles.getFiles();
}
```

This patch modifies the code to first call `scan()` and then get the `ClassFileSet` from `directoryScanner`. After that, it gets the files from `ClassFileSet` and returns them. This should fix the "cannot find symbol" error.