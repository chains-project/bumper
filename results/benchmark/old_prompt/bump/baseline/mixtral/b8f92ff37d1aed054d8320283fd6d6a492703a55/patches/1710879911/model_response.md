Here is a patch for the failing method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    ClasspathOptionScanner directoryScanner = new ClasspathOptionScanner(testSrcFolder, TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```
In the original code, `DirectoryScanner` is used which seems to be removed in the new version of the dependency. I replaced it with `ClasspathOptionScanner` which is a new addition in the new version. This should resolve the symbol error.