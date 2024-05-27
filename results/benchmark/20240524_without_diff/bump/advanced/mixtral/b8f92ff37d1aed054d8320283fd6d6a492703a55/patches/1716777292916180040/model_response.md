Here's a possible patch for the failing client code:
```java
import org.apache.maven.surefire.api.testset.TestFileSet;
import org.apache.maven.surefire.api.testset.TestFileSetBuilder;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    TestFileSetBuilder builder = new TestFileSetBuilder();
    TestFileSet testFileSet = builder.testFileSet(testSrcFolder).build();
    TestListResolver testListResolver = new TestListResolver(testFileSet);
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, testListResolver.getIncludes());
    return directoryScanner.scan().getClasses();
}
```
Explanation:
The issue with the original code is that the `getWildcard()` method is not available in the `TestListResolver` class. Instead, we can use the `TestFileSet` and `TestFileSetBuilder` classes to build a `TestFileSet` object, which can be passed to the `TestListResolver` constructor. We can then use the `getIncludes()` method to get the includes pattern, and pass it to the `DirectoryScanner` constructor. This should resolve the `cannot find symbol` error.
Note: I added the import statements, assuming that the classes are available in the classpath.