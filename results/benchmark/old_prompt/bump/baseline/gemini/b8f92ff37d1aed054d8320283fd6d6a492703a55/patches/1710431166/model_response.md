```java
  // TODO: review this AI generated patch!
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        directoryScanner.scan();
        return directoryScanner.getClasses();
    }
```