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
Explanation of the changes made:

* I replaced `DirectoryScanner` with `AntDirectoryScanner` which is a subclass of `DirectoryScanner` and is not deprecated.
* I set the `basedir` property of `AntDirectoryScanner` instead of passing it to the constructor since the constructor is deprecated.
* I replaced `scan().getClasses()` with `scan()` and then `getIncludedFiles()` to get the scanned files.

Note: I made these changes based on the assumption that there are no other dependencies or usage of this method that could be affected. If there are, further changes might be needed.