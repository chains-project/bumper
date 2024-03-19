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
In the original code, `DirectoryScanner` is an abstract class and it seems that it was removed or changed in the new version. I replaced it with `AntDirectoryScanner` which is a concrete implementation of the `DirectoryScanner` abstract class. Also, the method `scan()` should be called before `getClasses()` and the `getIncludedFiles()` should be used instead of `getClasses()` to get the files.