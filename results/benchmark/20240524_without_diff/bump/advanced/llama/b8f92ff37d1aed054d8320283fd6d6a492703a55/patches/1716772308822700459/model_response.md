```java
protected java.lang.String computeJacocoIncludes() {
    java.lang.StringBuilder includes = new java.lang.StringBuilder();
    for (java.lang.String directory : config.getBinJavaDir()) {
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), "**/*.class");
        includes.append(":").append(java.lang.String.join(":", directoryScanner.scan().getIncludedFiles()));
    }
    if (config.isCoverTests()) {
        for (java.lang.String directory : config.getBinTestDir()) {
            org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), "**/*.class");
            includes.append(":").append(java.lang.String.join(":", directoryScanner.scan().getIncludedFiles()));
        }
    }
    return includes.toString();
}
```