```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory), TestListResolver.getWildcard());
        List<Class> classes = directoryScanner.scan().getClasses();
        if (!classes.isEmpty()) {
            includes.append(":").append(classes.stream().reduce((x, y) -> x + ":" + y).orElse(""));
        }
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory), TestListResolver.getWildcard());
            List<Class> classes = directoryScanner.scan().getClasses();
            if (!classes.isEmpty()) {
                includes.append(":").append(classes.stream().reduce((x, y) -> x + ":" + y).orElse(""));
            }
        }
    }
    return includes.toString();
}
```