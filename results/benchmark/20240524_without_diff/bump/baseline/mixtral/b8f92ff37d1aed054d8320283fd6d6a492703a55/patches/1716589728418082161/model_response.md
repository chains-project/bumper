Here's a possible patch for the given code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(TestListResolver.getWildcard());
    directoryScanner.scan();
    return directoryScanner.getClasses();
}
```

This code creates a new `DirectoryScanner` instance and sets its properties explicitly, instead of passing them to the constructor. This should fix the issue with the missing symbol.