```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, "**/*.java");
    return directoryScanner.scan().getClasses();
}
```