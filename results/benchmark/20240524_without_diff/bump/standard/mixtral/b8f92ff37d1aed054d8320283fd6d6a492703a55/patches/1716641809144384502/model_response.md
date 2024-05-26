Here's the fixed `getClassesLoc` method with the required changes:

```java
import org.apache.maven.shared.utils.fn.FileUtils;
import java.io.File;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    Collection<File> files = FileUtils.getFiles(testSrcFolder, null, false);
    List<String> classes = new LinkedList<>();
    for (File file : files) {
        if (file.isFile() && file.getName().endsWith(".class")) {
            classes.add(file.getAbsolutePath());
        }
    }
    return classes;
}
```

In this fixed version, I removed the dependency on `org.apache.maven.surefire.api.testset.TestListResolver` and used `org.apache.maven.shared.utils.fn.FileUtils` to get the list of files in the given directory. Afterward, I filtered the files ending with `.class` and added them to the result list.