Here's the patched version of the `getClassesLoc` method that should fix the error:

```java
import org.apache.maven.shared.utils.os.Platform;
import org.codehaus.plexus.components.interactivity.Prompter;
import org.codehaus.plexus.util.FileUtils;

import java.io.File;
import java.io.FileFilter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

static List<String> getClassesLoc(File testSrcFolder) {
    Pattern inclPattern = Pattern.compile("**"); // use regex pattern to match all files
    FileFilter fileFilter = f -> f.isFile() && inclPattern.matcher(f.getAbsolutePath()).matches();
    File[] files = FileUtils.listFiles(testSrcFolder, fileFilter, null);
    List<String> classNames = new ArrayList<>();
    for (File file : files) {
        String fileName = file.getName();
        if (fileName.endsWith(".class")) {
            String className = fileName.substring(0, fileName.length() - 6).replace(File.separatorChar, '.');
            classNames.add(className);
        }
    }
    return classNames;
}
```

This version uses the `FileUtils` class from the `plexus-utils` library to list the files in the given directory, and then filters out the class files using a regex pattern. It then constructs the class names from the file names and returns the list of class names.

Note that this version of the method doesn't use the `DirectoryScanner` or `TestListResolver` classes from the `maven-surefire-plugin` library, which were causing the original error. Instead, it uses the `FileUtils` class from the `plexus-utils` library to list the files in the given directory.