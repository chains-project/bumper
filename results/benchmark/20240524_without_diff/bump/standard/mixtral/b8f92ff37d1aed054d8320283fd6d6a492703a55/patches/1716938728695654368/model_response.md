Here is a possible patch for the failing client code:

```java
import org.apache.maven.surefire.api.testset.TestFileSet;
import org.apache.maven.surefire.api.testset.TestListResolver;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new TestListResolver() {
        @Override
        public TestFileSet resolveTestFileSet(String arg0) {
            throw new UnsupportedOperationException("Not implemented");
        }

        @Override
        public String getWildcard() {
            return "**/*.class";
        }
    });
    return directoryScanner.scan().getClasses();
}
```

This patch creates an anonymous inner class that extends `TestListResolver` and overrides the `getWildcard()` method to return the string `"**/*.class"`. This should fix the error by providing the missing symbol `getWildcard()`. Note that the `resolveTestFileSet()` method is not used in this case, so it throws an `UnsupportedOperationException`.

Note that this patch may not be the most elegant or efficient solution, but it should make the code compile and run without errors.