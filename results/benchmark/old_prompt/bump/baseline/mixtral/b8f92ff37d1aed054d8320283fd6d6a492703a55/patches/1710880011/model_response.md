Here is a patch for the failing method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    AntDirectoryScanner directoryScanner = new AntDirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(TestListResolver.getWildcard());
    directoryScanner.scan();
    return directoryScanner.getIncludedFiles();
}
```
The failure is caused by using the `DirectoryScanner` class from a different package than before, which has been deprecated and removed. The `AntDirectoryScanner` class can be used instead, which has similar functionality. The method `setBasedir` is used to set the base directory to scan, `setIncludes` is used to set the wildcard pattern to match the files, and `scan` is used to scan the directory. Finally, the method `getIncludedFiles` is used to retrieve the list of included files.