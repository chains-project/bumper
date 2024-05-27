Here's a possible patch for the given client code:

```java
import org.apache.maven.surefire.api.testset.TestFileSet;
import org.apache.maven.surefire.api.testset.TestSetScannerContext;
import org.apache.maven.surefire.util.DefaultDirectoryScanner;
import org.apache.maven.surefire.util.DirectoryScanner;
import org.apache.maven.surefire.util.TestsToRun;

import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DefaultDirectoryScanner(testSrcFolder, new TestFileSet("", "", new TestsToRun()));
    directoryScanner.setIncludes(new String[]{"**/*.class"});
    return directoryScanner.scan().getIncludedFiles();
}
```

In this patch, we replaced the use of `TestListResolver.getWildcard()` with `new String[]{"**/*.class"}` to specify the pattern for including class files. We also replaced the `DirectoryScanner` constructor to accept a `TestFileSet` and `TestsToRun` instead of a `TestListResolver`. Finally, we called `setIncludes` on the `DirectoryScanner` to specify the include pattern.