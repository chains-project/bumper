```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    java.lang.String wildcard = "**/*Test.java";
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, wildcard);
    return directoryScanner.scan().getIncludedFilesList();
}
```