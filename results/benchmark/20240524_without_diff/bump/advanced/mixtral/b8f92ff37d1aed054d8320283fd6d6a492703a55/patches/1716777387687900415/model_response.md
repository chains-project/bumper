Here's the patched version of the code that should fix the error:

```java
import org.apache.maven.surefire.api.testset.TestFileSet;
import org.apache.maven.surefire.api.testset.TestListResolver;
import org.apache.maven.surefire.api.testset.TestSetFailedException;
import org.apache.maven.surefire.util.DefaultDirectoryScanner;
import org.apache.maven.surefire.util.DirectoryScanner;
import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DefaultDirectoryScanner(testSrcFolder, new TestFileSet());
    TestListResolver testListResolver = new TestListResolver();
    try {
        testListResolver.resolveTestSets(directoryScanner);
    } catch (TestSetFailedException e) {
        // Handle exception if needed
    }
    return directoryScanner.getIncludedFiles();
}
```

In this version, I replaced the `DirectoryScanner` constructor argument with a new `TestFileSet` object, and created a new `TestListResolver` object to call the `resolveTestSets` method.

After calling `resolveTestSets`, the `DirectoryScanner` object will have its list of included files updated, which we can retrieve using the `getIncludedFiles` method.

Note that the `TestListResolver` constructor takes a `TestFilter` object as an argument, which can be used to further customize the test set resolution. In this example, I passed a default `TestFileSet` object, which means that all files will be included.