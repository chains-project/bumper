Here is a fixed version of the `getClassesLoc` method:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver() {
        @Override
        protected String getWildcard() {
            return super.getWildcard();
        }
    }.getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The issue is caused by the fact that the `getWildcard()` method is no longer a static method. To fix this, I created an anonymous inner class that extends `TestListResolver` and overrides the `getWildcard()` method. This allows us to continue using the `getWildcard()` method in the same way as before, while still being compatible with the updated library.