```java
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class DirectoryScanner {
    private List<String> includes = new ArrayList<>();
    private List<String> excludes = new ArrayList<>();

    public void scan(File basedir) {
        // implementation
    }

    public List<String> getIncludedFiles() {
        return includes;
    }

    public List<String> getExcludedFiles() {
        return excludes;
    }
}
```