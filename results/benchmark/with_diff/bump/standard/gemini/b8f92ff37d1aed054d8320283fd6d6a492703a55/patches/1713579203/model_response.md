```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder);
    directoryScanner.setIncludes(new java.lang.String[] { "**/*.java" });
    return directoryScanner.scan().getClasses();
}
```