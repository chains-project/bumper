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

In this patch, I created a new instance of `DirectoryScanner` and then explicitly set the `basedir` and `includes` properties before scanning and retrieving the classes. This should fix the issue of the missing symbol, as the symbol is now being resolved through the new instance of `DirectoryScanner`.