Here's a fixed version of the `getClassesLoc` method that uses the `DirectoryScanner` class from the `org.apache.maven.shared` package instead of the `org.apache.maven.plugin.surefire.util` package:

```java
import org.apache.maven.shared.utils.io.DirectoryScanner;
import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder.getAbsolutePath());
    directoryScanner.setIncludes(new String[]{"**/*.class"});
    directoryScanner.scan();
    return directoryScanner.getIncludedFiles();
}
```

This version of the method uses the `DirectoryScanner` class from the `org.apache.maven.shared` package, which should be available even if the `org.apache.maven.plugin.surefire.util.DirectoryScanner` class is not available. The method sets the base directory of the scanner to the `testSrcFolder` parameter, sets the includes pattern to match all `.class` files, scans the directory, and returns the list of included files.