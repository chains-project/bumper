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

This patch modifies the `DirectoryScanner` constructor to use the default constructor, and sets the `basedir` and `includes` properties explicitly. This should ensure compatibility with newer versions of the external dependency that may have removed the constructor that takes a `File` argument.