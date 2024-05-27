Here's the proposed patch for the failing client code:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProviderFactory;
import org.apache.maven.surefire.api.testset.TestListResolver;
import org.apache.maven.surefire.api.util.SurefireReflectionUtils;

import java.io.File;
import java.lang.reflect.Method;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DefaultForkConfiguration forConfig = new DefaultForkConfiguration();
    Commandline commandLine = forConfig.createCommandLine(new StartupConfiguration(), 1, testSrcFolder);
    Class<?> commandLineClass = commandLine.getClass();
    Method getTestListResolverMethod = SurefireReflectionUtils.getMethod(commandLineClass, "getTestListResolver");
    TestListResolver testListResolver = (TestListResolver) SurefireReflectionUtils.invokeMethod(getTestListResolverMethod, commandLine);
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, testListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}

static class DirectoryScanner {
    private final File baseDir;
    private final String wildcard;

    DirectoryScanner(File baseDir, String wildcard) {
        this.baseDir = baseDir;
        this.wildcard = wildcard;
    }

    List<String> getClasses() {
        // Implement your logic to scan the baseDir using the wildcard and return the list of classes.
        // This example uses a placeholder implementation.
        return List.of("ClassA", "ClassB");
    }

    ScanResult scan() {
        return new ScanResult(baseDir, wildcard);
    }

    static class ScanResult {
        private final List<String> classes;

        ScanResult(File baseDir, String wildcard) {
            this.classes = getClasses();
        }

        List<String> getClasses() {
            // Implement your logic to scan the baseDir using the wildcard and return the list of classes.
            // This example uses a placeholder implementation.
            return List.of("ClassA", "ClassB");
        }
    }
}
```

This patch introduces a new helper class `DirectoryScanner` to handle the scanning of the test source folder. It uses reflection to access the `TestListResolver` from the `Commandline` object.

Additionally, the `getClasses()` method and a new `ScanResult` class are added to the `DirectoryScanner` class. These methods should be implemented according to your specific scanning logic.

Please note that this patch is just a suggestion, and you might need to adjust the code to fit your specific requirements.