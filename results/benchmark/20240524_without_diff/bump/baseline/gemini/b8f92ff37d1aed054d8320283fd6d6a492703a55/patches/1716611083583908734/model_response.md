```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    directoryScanner.scan();
    List<String> classes = directoryScanner.getClasses();
    if (classes == null) {
        return Collections.emptyList();
    }
    return classes;
}
```