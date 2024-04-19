```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getDefaultWildcard());
        return directoryScanner.scan().getClasses();
    }
```