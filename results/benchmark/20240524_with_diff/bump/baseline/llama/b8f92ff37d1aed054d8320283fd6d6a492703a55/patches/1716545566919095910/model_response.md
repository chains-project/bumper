```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, "**/*Test.class");
    return directoryScanner.scan().getClasses();
}
```