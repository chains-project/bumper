Here's the patched `getClassesLoc` method that should fix the error:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver() {
        protected String getWildcard() {
            return "**/*.class";
        }
    });
    return directoryScanner.scan().getClasses();
}
```

The change here is the creation of an anonymous class that extends `TestListResolver` and provides the `getWildcard` method. This should fix the error caused by the missing `getWildcard` method in the new version of the library.