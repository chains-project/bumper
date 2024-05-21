Here is a potential patch for the code:

```java
import org.apache.maven.surefire.api.util.DefaultScanResult;
import org.apache.maven.surefire.api.util.ScanResult;
import org.apache.maven.surefire.api.util.SurefireReflectionUtil;

import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, SurefireReflectionUtil.forName("org.apache.maven.surefire.api.testset.TestListResolver", SurefireReflectionUtil.class.getClassLoader()).getMethod("getWildcard", new Class[0]));
    return new DefaultScanResult(directoryScanner.scan()).getClasses();
}
```

This patch uses the `SurefireReflectionUtil` class to dynamically access the `getWildcard` method of the `TestListResolver` class, as the method is no longer directly available. It also uses the `DefaultScanResult` class to create a `ScanResult` object, as the constructor for `ScanResult` is now protected.