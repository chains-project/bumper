```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, org.apache.maven.surefire.api.testset.TestListResolver.TEST_LIST_RESOLVER_WILDCARD);
    return directoryScanner.scan().getClasses();
}
```