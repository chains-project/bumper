```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        File file = new File(directory);
        File[] files = file.listFiles((dir, name) -> name.endsWith(".class"));
        List<String> classNames = new ArrayList<>();
        for (File classFile : files) {
            classNames.add(classFile.getName().replace(".class", ""));
        }
        includes.append(String.join(":", classNames)).append(":");
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            File file = new File(directory);
            File[] files = file.listFiles((dir, name) -> name.endsWith(".class"));
            List<String> classNames = new ArrayList<>();
            for (File classFile : files) {
                classNames.add(classFile.getName().replace(".class", ""));
            }
            includes.append(String.join(":", classNames)).append(":");
        }
    }
    return includes.toString();
}
```