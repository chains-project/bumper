```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    // ++ added library method to scan for java files
    directoryScanner.setIncludes(new String[]{"**/*.java"});
    directoryScanner.scan();
    return directoryScanner.getClasses();
}
```