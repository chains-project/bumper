Here's the updated method with the necessary changes to fix the error:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booter.StartupConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.CommandlineConfiguration;
import org.apache.maven.plugin.surefire.util.DefaultDirectoryScanner;
import org.apache.maven.plugin.surefire.util.DefaultScanResult;
import org.apache.maven.plugin.surefire.util.SurefireReflectionUtils;

import java.io.File;
import java.lang.reflect.Method;
import java.util.Collections;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DefaultDirectoryScanner directoryScanner = new DefaultDirectoryScanner(testSrcFolder, getTestListResolverWildcard());
    return directoryScanner.scan().getClasses();
}

private static String getTestListResolverWildcard() {
    Class<?> testListResolverClass;
    Method getWildcardMethod;
    try {
        testListResolverClass = Class.forName("org.apache.maven.surefire.api.testset.TestListResolver");
        getWildcardMethod = testListResolverClass.getDeclaredMethod("getWildcard");
    } catch (ClassNotFoundException | NoSuchMethodException e) {
        throw new RuntimeException("Failed to get TestListResolver.getWildcard()", e);
    }

    return (String) SurefireReflectionUtils.invokeMethod(getWildcardMethod, null);
}
```

The main change is that the code now uses reflection to access the `getWildcard()` method since it's no longer directly accessible. The `DefaultDirectoryScanner` is used instead of `DirectoryScanner` since it is the implementation used by `DirectoryScanner`. Also, the `DefaultScanResult` is used instead of the deprecated `ScanResult`.