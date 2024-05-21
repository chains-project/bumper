Here is a potential patch for the given client code:
```java
import org.apache.maven.shared.utils.StringUtils;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, StringUtils.patternMatcher("**/*.class"));
    return directoryScanner.scan().getIncludedFiles();
}

static class DirectoryScanner {
    private File baseDir;
    private Pattern pattern;

    DirectoryScanner(File baseDir, String pattern) {
        this.baseDir = baseDir;
        this.pattern = Pattern.compile(pattern);
    }

    List<String> scan() {
        List<String> result = new ArrayList<>();
        File[] files = baseDir.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    DirectoryScanner subDirectoryScanner = new DirectoryScanner(file, pattern.pattern());
                    result.addAll(subDirectoryScanner.scan());
                } else if (pattern.matcher(file.getName()).matches()) {
                    result.add(file.getAbsolutePath());
                }
            }
        }
        return result;
    }

    List<String> getIncludedFiles() {
        return getFiles();
    }
}
```
The patch replaces the usage of the `DirectoryScanner` class from the `org.apache.maven.plugin.surefire.util` package with a custom implementation. The custom implementation uses the `StringUtils` class from the `org.apache.maven.shared.utils` package to create a pattern matcher for the `DirectoryScanner` class. The `DirectoryScanner` class then recursively scans the directory structure for files that match the specified pattern.

Note that the custom implementation may not have the same performance characteristics as the original implementation. It is important to thoroughly test the updated code to ensure that it meets the desired requirements.