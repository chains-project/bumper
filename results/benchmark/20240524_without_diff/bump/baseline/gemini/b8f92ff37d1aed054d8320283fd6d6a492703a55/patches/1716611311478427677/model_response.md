```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = new ArrayList<>();
        for (String file : directoryScanner.scan().getFiles()) {
            if (file.endsWith(".java")) {
                classes.add(file);
            }
        }
        return classes;
    }
```