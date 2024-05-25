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

This patch uses the default constructor of `DirectoryScanner` and sets the `basedir` and `includes` properties explicitly. This should work even if the constructor that takes a `File` and a `String` has been removed.