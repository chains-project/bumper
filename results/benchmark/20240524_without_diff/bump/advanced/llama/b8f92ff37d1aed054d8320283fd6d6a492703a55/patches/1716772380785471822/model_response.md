```java
protected java.lang.String computeJacocoIncludes() {
    java.lang.StringBuilder includes = new java.lang.StringBuilder();
    for (java.lang.String directory : config.getBinJavaDir()) {
        org.apache.maven.shared.utils.cli.Commandline pattern = new org.apache.maven.shared.utils.cli.Commandline();
        pattern.createArg().setValue("**/*.class");
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), pattern);
        includes.append(":").append(directoryScanner.scan().getIncludedFiles().stream().map(file -> file.getName()).reduce(( x, y) -> (x + ":") + y).orElse(""));
    }
    if (config.isCoverTests()) {
        for (java.lang.String directory : config.getBinTestDir()) {
            org.apache.maven.shared.utils.cli.Commandline pattern = new org.apache.maven.shared.utils.cli.Commandline();
            pattern.createArg().setValue("**/*.class");
            org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), pattern);
            includes.append(":").append(directoryScanner.scan().getIncludedFiles().stream().map(file -> file.getName()).reduce(( x, y) -> (x + ":") + y).orElse(""));
        }
    }
    return includes.toString();
}
```