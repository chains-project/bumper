Here's the updated method with the changes to fix the error:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.surefire.api.testset.TestListResolver;
import org.apache.maven.surefire.booter.StartupConfiguration;

import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    StartupConfiguration config = new StartupConfiguration();
    Commandline commandLine = new DefaultForkConfiguration().createCommandLine(config, 0, testSrcFolder);
    TestListResolver testListResolver = new TestListResolver();
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, testListResolver.getWildcard());
    directoryScanner.scan();
    return directoryScanner.getClasses();
}
```

The changes include:

1. Importing the required classes for `Commandline` and `DefaultForkConfiguration`.
2. Creating a `StartupConfiguration` object `config`.
3. Replacing `OutputStreamFlushableCommandline` with `Commandline` for `createCommandLine`.
4. Creating a `TestListResolver` object `testListResolver`.
5. Using `testListResolver.getWildcard()` instead of `TestListResolver.getWildcard()`.