Here is a possible patch for the failing client code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    Collection<String> classes = directoryScanner.scan().getClasses();
    return new ArrayList<>(classes);
}
```

This patch creates a new `ArrayList` from the `Collection` of classes returned by the `scan()` method. This is because the `getClasses()` method has been removed in the new version of the library, and has been replaced by the `scan()` method which returns a `Collection` of classes.

Note that this patch assumes that the `DirectoryScanner` class and the `TestListResolver` class are still available and unchanged in the new version of the library. If this is not the case, then further changes may be necessary.