```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    ++ directoryScanner.setIncludes(new String[] {"**/*.java"});
    return directoryScanner.scan().getClasses();
}
```