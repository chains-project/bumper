```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = directoryScanner.scan().getClasses();
        if (classes == null) {
            classes = new ArrayList<>();
        }
        return classes;
    }
```