```java
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class DirectoryScanner {
    public List<String> scan(String basedir) {
        List<String> files = new ArrayList<>();
        File dir = new File(basedir);
        for (File file : dir.listFiles()) {
            if (file.isFile()) {
                files.add(file.getName());
            }
        }
        return files;
    }
}
```