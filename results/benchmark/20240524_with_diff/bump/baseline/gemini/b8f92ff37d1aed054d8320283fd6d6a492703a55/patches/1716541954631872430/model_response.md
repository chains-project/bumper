```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder);
        directoryScanner.setIncludes(new String[] {"**/*.java"});
        directoryScanner.scan();
        return directoryScanner.getIncludedFiles();
    }
```