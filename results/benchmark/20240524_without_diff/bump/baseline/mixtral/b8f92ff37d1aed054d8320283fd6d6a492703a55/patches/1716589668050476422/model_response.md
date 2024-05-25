Here's a possible patch for the given client code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(TestListResolver.getWildcard());
    directoryScanner.scan();
    return directoryScanner.getClasses();
}
```

This patch initializes the `DirectoryScanner` with a no-arg constructor, and then sets the `basedir` and `includes` properties explicitly. This should avoid any issues with the constructor that takes a `File` and a `String` argument.