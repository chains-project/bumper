Here is a possible patch for the code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    ClasspathScanner directoryScanner = new ClasspathScanner(testSrcFolder, TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```

This patch replaces the `DirectoryScanner` class with the `ClasspathScanner` class, which is a new class added in the external dependency. The `ClasspathScanner` class has the same methods as the `DirectoryScanner` class, so the rest of the code can stay the same. This should fix the "cannot find symbol" error.