```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    java.util.ArrayList<java.lang.String> wildcards = new java.util.ArrayList<>();
    wildcards.add("**/*.class");
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, wildcards);
    return directoryScanner.scan().getIncludedFilesList();
}
```