Here is the patched code:

```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        File dir = new File(directory);
        List<String> classes = new ArrayList<>();
        for (File file : dir.listFiles()) {
            if (file.isFile() && file.getName().endsWith(".class")) {
                classes.add(file.getName().replace(".class", ""));
            }
        }
        includes.append(":").append(String.join(":", classes));
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            File dir = new File(directory);
            List<String> classes = new ArrayList<>();
            for (File file : dir.listFiles()) {
                if (file.isFile() && file.getName().endsWith(".class")) {
                    classes.add(file.getName().replace(".class", ""));
                }
            }
            includes.append(":").append(String.join(":", classes));
        }
    }
    return includes.toString();
}
```