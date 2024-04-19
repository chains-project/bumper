Here's a fixed version of the `getClassesLoc` method that uses an added library method `getIncludes` instead of the removed `getWildcard` method:

```java
import org.apache.maven.plugin.surefire.util.DefaultDirectoryScanner;
import org.apache.maven.plugin.surefire.util.DirectoryScanner;

import java.io.File;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DefaultDirectoryScanner(testSrcFolder);
    directoryScanner.setIncludes(new String[]{"**/*.class"});
    return directoryScanner.scan().getClasses();
}
```

Note that I've changed the `DirectoryScanner` implementation to `DefaultDirectoryScanner` which has the `setIncludes` method that can be used instead of `getWildcard`. Also, I've set the includes to match all class files using the pattern `"**/*.class"`.