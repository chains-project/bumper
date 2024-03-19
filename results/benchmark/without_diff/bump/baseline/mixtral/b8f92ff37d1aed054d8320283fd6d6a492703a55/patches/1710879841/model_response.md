Here is a patch for the failing method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    AntDirectoryScanner directoryScanner = new AntDirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(new String[]{TestListResolver.getWildcard()});
    directoryScanner.scan();
    return directoryScanner.getIncludedFiles();
}
```
In the previous code, I replaced `DirectoryScanner` with `AntDirectoryScanner` which is the added class in the new version. Also, I replaced `DirectoryScanner.scan()` with `directoryScanner.scan()` and `directoryScanner.getClasses()` with `directoryScanner.getIncludedFiles()` as these methods are no longer exist in the new version.