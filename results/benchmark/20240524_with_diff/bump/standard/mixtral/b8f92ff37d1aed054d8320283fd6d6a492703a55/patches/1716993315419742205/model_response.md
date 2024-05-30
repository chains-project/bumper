Here is a potential patch for the failing client code:
```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProviderUtils;
import org.apache.maven.surefire.api.testset.TestListResolver;
import org.apache.maven.surefire.api.util.SurefireReflectionUtils;

import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DefaultForkConfiguration forConfig = new DefaultForkConfiguration();
    Commandline commandLine = forConfig.createCommandLine(new StartupConfiguration(), 1, testSrcFolder);
    TestListResolver testListResolver = SurefireReflectionUtils.getInstance(commandLine, TestListResolver.class);
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, testListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}

static class DirectoryScanner {
    private final File baseDirectory;
    private final String wildcard;

    public DirectoryScanner(File baseDirectory, String wildcard) {
        this.baseDirectory = baseDirectory;
        this.wildcard = wildcard;
    }

    public DirectoryScanner scan() {
        // Implementation of the scanning logic using the baseDirectory and wildcard
        // ...
        return this;
    }

    public List<String> getClasses() {
        // Implementation of the logic to get the classes
        // ...
        return null;
    }
}
```
Explanation:

The patch creates a new class `DirectoryScanner` that encapsulates the scanning logic. This allows us to manually create an instance of `TestListResolver` and use its `getWildcard()` method.

We also create a `Commandline` instance using the `DefaultForkConfiguration` class, which is a replacement for the deprecated `OutputStreamFlushableCommandline` type.

Finally, we use the `SurefireReflectionUtils` class to get an instance of `TestListResolver` from the `Commandline` object. This allows us to call the `getWildcard()` method and pass it to the `DirectoryScanner` constructor.

Note: This patch assumes that the scanning and class retrieval logic is implemented in the `DirectoryScanner` class. You will need to implement this logic according to your specific requirements.