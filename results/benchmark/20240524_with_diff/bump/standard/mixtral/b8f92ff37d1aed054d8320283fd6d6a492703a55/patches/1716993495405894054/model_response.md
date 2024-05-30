Here's a possible patch for the client code to fix the error:

```java
protected java.lang.String computeJacocoIncludes() {
    java.lang.StringBuilder includes = new java.lang.StringBuilder();
    for (java.lang.String directory : config.getBinJavaDir()) {
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), getWildcard());
        includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
    }
    if (config.isCoverTests()) {
        for (java.lang.String directory : config.getBinTestDir()) {
            org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), getWildcard());
            includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
        }
    }
    return includes.toString();
}

private static String getWildcard() {
    return "**/*.class";
}
```

The patch adds a new private method `getWildcard()` that returns the wildcard string used in the `DirectoryScanner` constructor. This way, the client code no longer depends on the `TestListResolver` class, which was removed in the new library version.