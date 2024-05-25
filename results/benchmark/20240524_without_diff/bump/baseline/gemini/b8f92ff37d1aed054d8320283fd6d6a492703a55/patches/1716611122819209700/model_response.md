```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        directoryScanner.setClassLoader(TestListResolver.getClassLoader()); // Add class loader to directory scanner
        return directoryScanner.scan().getClasses();
    }
```