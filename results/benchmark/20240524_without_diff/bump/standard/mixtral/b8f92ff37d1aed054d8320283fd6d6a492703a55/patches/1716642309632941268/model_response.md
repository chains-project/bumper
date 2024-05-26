Here's a fixed version of the `computeJacocoIncludes` method that replaces the usage of the deprecated `getWildcard` method:

```java
protected java.lang.String computeJacocoIncludes() {
    java.lang.StringBuilder includes = new java.lang.StringBuilder();
    for (java.lang.String directory : config.getBinJavaDir()) {
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), "*");
        includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
    }
    if (config.isCoverTests()) {
        for (java.lang.String directory : config.getBinTestDir()) {
            org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), "*");
            includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
        }
    }
    return includes.toString();
}
```

The change is simply replacing `org.apache.maven.surefire.api.testset.TestListResolver.getWildcard()` with a `*` character. This is because the `getWildcard` method has been deprecated and removed from the library. The `*` character is a valid argument for the `DirectoryScanner` constructor and serves the same purpose as the deprecated method.