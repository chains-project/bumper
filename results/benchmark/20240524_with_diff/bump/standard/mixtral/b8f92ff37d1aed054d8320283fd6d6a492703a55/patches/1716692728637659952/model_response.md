Here's the fixed `getClassesLoc` method using the new library version:

```java
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.Commandline;
import org.apache.maven.surefire.api.testset.TestListResolver;
import org.apache.maven.surefire.api.testset.TestSetFailedException;
import org.apache.maven.surefire.util.DefaultScanResult;
import org.apache.maven.surefire.util.ScanResult;
import org.apache.maven.surefire.util.SurefireReflectionUtils;

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DefaultForkConfiguration defaultForkConfiguration = new DefaultForkConfiguration();
    Commandline commandLine = defaultForkConfiguration.createCommandLine(new StartupConfiguration(), 0, testSrcFolder.getParentFile());
    TestListResolver testListResolver = SurefireReflectionUtils.getInstanceOf(TestListResolver.class, commandLine);
    String wildcard = testListResolver.getWildcard();
    ScanResult scanResult = new DefaultScanResult(testSrcFolder, wildcard);
    try {
        scanResult.scan();
    } catch (TestSetFailedException e) {
        throw new RuntimeException("Failed to scan test sources", e);
    }
    List<String> classes = new ArrayList<>();
    for (ScanResult.FileSet fileSet : scanResult.getFileSets()) {
        Collections.addAll(classes, fileSet.getClasses());
    }
    return classes;
}
```

I created a `Commandline` instance using `DefaultForkConfiguration` and extracted `TestListResolver` from it. This allows us to use `TestListResolver` to get the wildcard. Also, I replaced the deprecated `DirectoryScanner` with `ScanResult` and iterated over `fileSets` to get the classes.