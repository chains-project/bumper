```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        ++directoryScanner.setIncludeSubdirectories(true);
        return directoryScanner.scan().getClasses();
    }
```