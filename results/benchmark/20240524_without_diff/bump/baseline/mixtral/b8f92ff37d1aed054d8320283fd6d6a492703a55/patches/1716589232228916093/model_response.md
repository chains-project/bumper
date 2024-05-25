Here's a possible patch for the given code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    ClasspathScanner directoryScanner = new ClasspathScanner(testSrcFolder, TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```

In this patch, I replaced `DirectoryScanner` with `ClasspathScanner` which is an added library method identified with `++`. This should fix the "cannot find symbol" error.