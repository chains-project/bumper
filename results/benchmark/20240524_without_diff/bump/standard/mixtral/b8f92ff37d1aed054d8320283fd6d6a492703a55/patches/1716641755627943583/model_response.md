Here is a possible patch for the code:

```java
import org.apache.maven.surefire.api.testset.TestFileSet;
import org.apache.maven.surefire.api.util.SurefireReflectionUtils;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getTestFileSet().getIncludes());
    return directoryScanner.scan().getClasses();
}

private static TestFileSet getTestFileSet() {
    return SurefireReflectionUtils.getInstance().newInstance(TestFileSet.class);
}
```

In this patch, I created a new method `getTestFileSet()` that returns a new instance of `TestFileSet` using the `SurefireReflectionUtils` class. Then, I used the `getIncludes()` method of the `TestFileSet` class instead of the `getWildcard()` method of the `TestListResolver` class, which seems to be no longer available. This should fix the "cannot find symbol" error.