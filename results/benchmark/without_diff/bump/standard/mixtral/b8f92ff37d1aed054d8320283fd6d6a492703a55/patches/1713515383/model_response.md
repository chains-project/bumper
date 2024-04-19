Here's the patched version of the `getClassesLoc` method that uses a different approach to get the wildcard, avoiding the usage of the removed `getWildcard()` method from `TestListResolver`:

```java
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import org.apache.maven.plugin.surefire.util.DefaultDirectoryScanner;
import org.apache.maven.plugin.surefire.util.DirectoryScanner;
import org.apache.maven.shared.utils.StringUtils;

static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DefaultDirectoryScanner(testSrcFolder);
    String[] includes = new String[]{"**/*.class"};
    directoryScanner.setIncludes(includes);
    directoryScanner.scan();

    List<String> classes = new ArrayList<>();
    String[] files = directoryScanner.getIncludedFiles();
    for (String file : files) {
        classes.add(StringUtils.substringBeforeLast(file, "."));
    }

    return classes;
}
```

This version uses the `DefaultDirectoryScanner` class, which is a subclass of `DirectoryScanner`. It sets the includes to match all the class files using a regex pattern. After scanning, it collects the matched class names and returns the list.