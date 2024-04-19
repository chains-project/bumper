Here is a possible patch for the failing client code:

```java
import org.apache.maven.shared.utils.os.PathUtil;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

static List<String> getClassesLoc(File testSrcFolder) {
    File[] files = testSrcFolder.listFiles();
    List<File> matchingFiles = new ArrayList<>();
    for (File file : files) {
        if (file.isDirectory() && file.getName().startsWith("**")) {
            matchingFiles.add(file);
        }
    }
    List<String> classNames = new ArrayList<>();
    for (File file : matchingFiles) {
        classNames.addAll(getClasses(file));
    }
    return classNames;
}

static List<String> getClasses(File dir) {
    return PathUtil.getFiles(dir, "**", null, false, true).stream()
        .filter(File::isFile)
        .filter(file -> file.getAbsolutePath().endsWith(".class"))
        .map(File::getAbsolutePath)
        .map(path -> path.substring(path.lastIndexOf('/') + 1, path.length() - 6))
        .collect(Collectors.toList());
}
```

The patch removes the dependency on `org.apache.maven.surefire.api.testset.TestListResolver` and replaces it with a custom implementation using Java 8 streams. The new implementation scans the given directory recursively and returns a list of class names based on the class files found.

Note that the new implementation may not be equivalent to the original implementation in terms of performance or functionality. It is up to you to test and validate the new implementation to ensure that it meets your requirements.