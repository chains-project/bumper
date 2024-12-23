Here is a possible patch for the failing client code:

```java
import org.apache.maven.surefire.api.testset.TestFileSet;
import org.apache.maven.surefire.api.testset.TestFileSetFactory;
import org.apache.maven.surefire.api.testset.TestListResolver;
import org.apache.maven.surefire.api.testset.TestListResolverFactory;

import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    TestFileSetFactory testFileSetFactory = new TestFileSetFactory();
    TestFileSet testFileSet = testFileSetFactory.create(testSrcFolder);
    TestListResolverFactory testListResolverFactory = new TestListResolverFactory();
    TestListResolver testListResolver = testListResolverFactory.createResolver(testFileSet);
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, testListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```

This patch creates instances of `TestFileSetFactory` and `TestListResolverFactory` to obtain instances of `TestFileSet` and `TestListResolver`, respectively. Then, it uses the `getWildcard()` method of `TestListResolver` to get the wildcard and pass it to the `DirectoryScanner` constructor.

Note that this patch assumes that the required classes and methods have been added to the project. If not, they need to be added as dependencies in the project's build tool configuration.