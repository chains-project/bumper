Here is a possible patch for the given code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(TestListResolver.getWildcard());
    directoryScanner.scan();
    return directoryScanner.getClasses();
}
```

This patch uses the default constructor of `DirectoryScanner` and sets the `basedir` and `includes` properties explicitly. This should fix the error caused by the missing symbol in the original code.