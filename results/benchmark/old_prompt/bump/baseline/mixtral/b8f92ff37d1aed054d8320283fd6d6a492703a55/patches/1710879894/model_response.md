Here is a patch for the failing method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    AntDirectoryScanner directoryScanner = new AntDirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(Arrays.asList("**/*.class"));
    directoryScanner.scan();
    return directoryScanner.getIncludedFiles();
}
```
Explanation:

* I replaced `DirectoryScanner` with `AntDirectoryScanner` which is a subclass that should still be available.
* I set the base directory using `setBasedir` method.
* I set the includes pattern using `setIncludes` method to scan for all class files.
* I called the `scan` method to perform the scan.
* I returned the included files using `getIncludedFiles` method.

Note: I can't be sure if this patch will work without more context about the codebase, but it should give you a good starting point.