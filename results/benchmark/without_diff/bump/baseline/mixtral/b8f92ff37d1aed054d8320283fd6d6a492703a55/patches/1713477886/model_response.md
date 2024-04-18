Sure, here's a potential patch for the failing client code:
```java
    static List<String> getClassesLoc(File testSrcFolder) {
        AntDirectoryScanner directoryScanner = new AntDirectoryScanner();
        directoryScanner.setBasedir(testSrcFolder);
        directoryScanner.setIncludes(TestListResolver.getWildcard());
        directoryScanner.scan();
        return directoryScanner.getIncludedFiles();
    }
```
In this patch, I've replaced the `DirectoryScanner` class with `AntDirectoryScanner`, which is a new class added in the external dependency. I've also replaced the `scan()` method with `getIncludedFiles()` to get the list of classes.

Note that I've added the necessary setter methods to configure the `AntDirectoryScanner` object.

This patch should fix the "cannot find symbol" error you were seeing.