```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        File file = new File(directory);
        List<File> files = new ArrayList<>();
        File[] filesInDir = file.listFiles();
        if (filesInDir != null) {
            for (File f : filesInDir) {
                if (f.isFile() && f.getName().endsWith(".class")) {
                    files.add(f);
                }
            }
        }
        for (File f : files) {
            includes.append(":").append(f.getName().replace(".class", ""));
        }
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            File file = new File(directory);
            List<File> files = new ArrayList<>();
            File[] filesInDir = file.listFiles();
            if (filesInDir != null) {
                for (File f : filesInDir) {
                    if (f.isFile() && f.getName().endsWith(".class")) {
                        files.add(f);
                    }
                }
            }
            for (File f : files) {
                includes.append(":").append(f.getName().replace(".class", ""));
            }
        }
    }
    return includes.toString();
}
```