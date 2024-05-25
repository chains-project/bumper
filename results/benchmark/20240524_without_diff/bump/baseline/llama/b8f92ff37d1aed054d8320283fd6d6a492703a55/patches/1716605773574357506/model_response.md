```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        File dir = new File(directory);
        String[] classes = dir.list((dir1, name) -> name.endsWith(".class"));
        includes.append(String.join(":", classes)).append(":");
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            File dir = new File(directory);
            String[] classes = dir.list((dir1, name) -> name.endsWith(".class"));
            includes.append(String.join(":", classes)).append(":");
        }
    }
    return includes.toString().replaceAll(":$", "");
}
```