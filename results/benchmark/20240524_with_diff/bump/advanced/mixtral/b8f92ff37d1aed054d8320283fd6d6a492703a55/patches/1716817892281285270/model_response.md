Here's the proposed patch for the failing client code:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProviderFactory;
import org.apache.maven.surefire.api.testset.TestRequest;
import org.apache.maven.surefire.api.testset.TestSetFailedException;
import org.apache.maven.surefire.api.util.SurefireReflectionUtils;

import java.io.File;
import java.util.Collection;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DefaultForkConfiguration forkedConfig = new DefaultForkConfiguration();
    TestRequest testRequest = new TestRequest();
    testRequest.setMethodName("getWildcard");
    Commandline commandLine = forkedConfig.createCommandLine(forkedConfig.getStartupConfiguration(), 0, testSrcFolder);
    LazyTestProviderFactory testProviderFactory = new LazyTestProviderFactory();
    try {
        Collection<File> testFiles = testProviderFactory.createTestProvider(commandLine, testSrcFolder, testRequest).getIncludedClasses();
        return SurefireReflectionUtils.getFileNames(testFiles);
    } catch (TestSetFailedException e) {
        throw new RuntimeException("Failed to scan test files", e);
    }
}
```

This patch replaces the usage of `DirectoryScanner` with a combination of `DefaultForkConfiguration`, `TestRequest`, `LazyTestProviderFactory`, and `SurefireReflectionUtils` to achieve the same functionality. The `getWildcard` method is now called dynamically using reflection.

To use this patch, replace the entire `getClassesLoc` method with the provided code.