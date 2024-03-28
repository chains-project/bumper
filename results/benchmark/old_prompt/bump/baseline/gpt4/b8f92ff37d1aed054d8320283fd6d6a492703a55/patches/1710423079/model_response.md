```java
static List<String> getClassesLoc(File testSrcFolder) {
    TestListResolver testListResolver = new TestListResolver();
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, testListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```