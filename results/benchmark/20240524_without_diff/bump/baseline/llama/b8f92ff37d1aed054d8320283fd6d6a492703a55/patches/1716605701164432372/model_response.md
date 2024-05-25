```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        File dir = new File(directory);
        if (dir.isDirectory()) {
            List<File> files = Arrays.asList(dir.listFiles());
            for (File file : files) {
                if (file.isFile() && file.getName().endsWith(".class")) {
                    includes.append(":").append(file.getName().replace(".class", ""));
                }
            }
        }
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            File dir = new File(directory);
            if (dir.isDirectory()) {
                List<File> files = Arrays.asList(dir.listFiles());
                for (File file : files) {
                    if (file.isFile() && file.getName().endsWith(".class")) {
                        includes.append(":").append(file.getName().replace(".class", ""));
                    }
                }
            }
        }
    }
    return includes.toString();
}
```