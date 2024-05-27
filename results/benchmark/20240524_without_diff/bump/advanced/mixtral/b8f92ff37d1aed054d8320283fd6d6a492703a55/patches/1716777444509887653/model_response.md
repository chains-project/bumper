Here's a possible patch for the given client code:

```java
import java.io.File;
import java.util.List;
import java.util.regex.Pattern;

import org.apache.maven.shared.utils.StringUtils;
import org.apache.maven.shared.utils.regexp.RegexpUtils;

static List<String> getClassesLoc(File testSrcFolder) {
    String[] includes = new String[]{"**/*.class"};
    String[] excludes = new String[]{};
    Pattern includePattern = StringUtils.translatePattern(includes, ",");
    Pattern excludePattern = StringUtils.translatePattern(excludes, ",");
    RegexpUtils regexpUtils = new RegexpUtils();
    List<String> classes = regexpUtils.getFiles(testSrcFolder.getAbsolutePath(), includePattern, excludePattern);
    return classes;
}
```

This patch replaces the usage of the `TestListResolver` class with the `RegexpUtils` class, which provides similar functionality. The `getWildcard()` method has been replaced with the `getFiles()` method, which takes include and exclude patterns as arguments. The `StringUtils` class is used to translate the include and exclude patterns from Ant-style wildcards to regular expressions. The `File` class is used to represent the test source folder.