```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, org.apache.maven.surefire.api.testset.TestListResolver.getWildcard());
    directoryScanner.scan();
    java.util.List<java.io.File> classes = directoryScanner.getClasses();
    java.util.List<java.lang.String> result = new java.util.ArrayList<>();
    for (java.io.File file : classes) {
        result.add(file.getAbsolutePath());
    }
    return result;
}
```