```java
protected String computeJacocoIncludes() {
    StringBuilder includes = new StringBuilder();
    for (String directory : config.getBinJavaDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory), TestListResolver.getWildcard());
        includes.append(":").append(String.join(":", directoryScanner.scan().getClasses()));
    }
    if (config.isCoverTests()) {
        for (String directory : config.getBinTestDir()) {
            DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory), TestListResolver.getWildcard());
            includes.append(":").append(String.join(":", directoryScanner.scan().getClasses()));
        }
    }
    return includes.toString();
}
```