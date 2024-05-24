```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory), TestListResolver.getWildcard());
        includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce((x, y) -> x + ":" + y).orElse(""));
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory), TestListResolver.getWildcard());
            includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce((x, y) -> x + ":" + y).orElse(""));
        }
    }
    return includes.toString();
}
```