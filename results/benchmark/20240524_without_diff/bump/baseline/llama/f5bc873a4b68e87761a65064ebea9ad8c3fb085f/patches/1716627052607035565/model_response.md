```java
import java.io.File;
import java.io.FileFilter;
import java.util.ArrayList;
import java.util.List;

public class DirectoryScanner {
    private File basedir;
    private List<String> includes = new ArrayList<>();
    private List<String> excludes = new ArrayList<>();

    public DirectoryScanner(String basedir) {
        this.basedir = new File(basedir);
    }

    public void setIncludes(String[] includes) {
        for (String include : includes) {
            this.includes.add(include);
        }
    }

    public void setExcludes(String[] excludes) {
        for (String exclude : excludes) {
            this.excludes.add(exclude);
        }
    }

    public List<File> scan() {
        List<File> files = new ArrayList<>();
        scan(this.basedir, files);
        return files;
    }

    private void scan(File dir, List<File> files) {
        for (File file : dir.listFiles(new FileFilter() {
            @Override
            public boolean accept(File file) {
                String name = file.getName();
                if (file.isDirectory()) {
                    return true;
                }
                for (String include : includes) {
                    if (name.matches(include)) {
                        for (String exclude : excludes) {
                            if (name.matches(exclude)) {
                                return false;
                            }
                        }
                        files.add(file);
                        return true;
                    }
                }
                return false;
            }
        })) {
            if (file.isDirectory()) {
                scan(file, files);
            }
        }
    }
}
```