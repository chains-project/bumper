```java
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class DirectoryScanner {
    public void scan() {
        List<String> includes = new ArrayList<>();
        includes.add("**/*.java");
        File basedir = new File(".");
        List<File> files = new ArrayList<>();
        scan(basedir, includes, files);
    }

    private void scan(File basedir, List<String> includes, List<File> files) {
        for (String include : includes) {
            File file = new File(basedir, include);
            if (file.isDirectory()) {
                File[] filesInDir = file.listFiles();
                for (File f : filesInDir) {
                    scan(f, includes, files);
                }
            } else {
                files.add(file);
            }
        }
    }
}
```