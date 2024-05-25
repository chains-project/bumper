```java
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class DirectoryScanner {
    public List<String> scan(String directory) {
        List<String> files = new ArrayList<>();
        File dir = new File(directory);
        for (File file : dir.listFiles()) {
            if (file.isFile()) {
                files.add(file.getAbsolutePath());
            }
        }
        return files;
    }
}
```