```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        directoryScanner.scan();
        return Arrays.stream(directoryScanner.getIncludedFiles()).map(file -> file.substring(0, file.length() - 5)).collect(Collectors.toList());
    }
```