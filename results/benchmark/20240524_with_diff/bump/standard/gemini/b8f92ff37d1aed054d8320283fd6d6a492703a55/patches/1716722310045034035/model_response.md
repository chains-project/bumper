```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder);
    directoryScanner.addDefaultExcludes();
    directoryScanner.setIncludes(new String[]{"**/*.java"});
    return directoryScanner.scan().getClasses();
}
```