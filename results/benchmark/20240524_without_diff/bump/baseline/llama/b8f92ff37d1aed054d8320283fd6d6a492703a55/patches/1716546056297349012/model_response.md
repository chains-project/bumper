```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        includes.append(":").append(getClasses(directory));
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            includes.append(":").append(getClasses(directory));
        }
    }
    return includes.toString();
}

private String getClasses(String directory) {
    DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory), "**/*.class");
    return directoryScanner.scan().getClasses().stream().reduce((x, y) -> x + ":" + y).orElse("");
}
```