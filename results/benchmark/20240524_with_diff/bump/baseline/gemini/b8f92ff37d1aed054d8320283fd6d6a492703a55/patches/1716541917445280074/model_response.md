```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, "**/*Test.java");
        return directoryScanner.scan().getClasses();
    }
```