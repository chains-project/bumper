```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = DirectoryScanner.create(testSrcFolder, TestListResolver.getWildcard());
        return directoryScanner.scan().getClasses();
    }
```