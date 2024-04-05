Here's a possible patch for the given failing method:
```java
import org.apache.maven.surefire.api.util.DefaultScanResult.ClasspathEntry;
import org.apache.maven.surefire.api.util.ScanResult;
import org.apache.maven.shared.utils.reflection.ReflectionUtils;

import java.io.File;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

static List<String> getClassesLoc(File testSrcFolder) {
    ClasspathEntry classpathEntry = new ClasspathEntry(testSrcFolder.getAbsolutePath(), null);
    ScanResult scanResult = new ScanResult(Arrays.asList(classpathEntry), null);
    Method getWildcardMethod;
    try {
        getWildcardMethod = ReflectionUtils.findMethod(TestListResolver.class, "getWildcard");
    } catch (Exception e) {
        throw new RuntimeException("Failed to find getWildcard method", e);
    }
    Object wildcard = ReflectionUtils.invokeMethod(getWildcardMethod, null);
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, wildcard);
    return directoryScanner.scan().getClasses();
}
```
This patch uses the `ReflectionUtils` class from Apache Commons Lang to invoke the `getWildcard` method of `TestListResolver` dynamically. It first finds the method using `ReflectionUtils.findMethod()`, then invokes it using `ReflectionUtils.invokeMethod()`.

Note that this patch uses reflection, which can be slower and less type-safe than regular method calls. It's recommended to use it only as a workaround until the external dependency is fixed.