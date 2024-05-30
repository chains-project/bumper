Here's the proposed patch for the provided code. I created a new `DirectoryScanner` instance outside of the for-loop and reused it for both directories. I also replaced the deprecated `getWildcard()` method with a hardcoded wildcard string.

Please note that this patch assumes that the `config` object has the necessary getter methods.

```java
protected java.lang.String computeJacocoIncludes() {
    java.lang.StringBuilder includes = new java.lang.StringBuilder();
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(config.getBinJavaDir().get(0)), "*");
    for (java.lang.String directory : config.getBinJavaDir()) {
        includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
    }
    if (config.isCoverTests()) {
        for (java.lang.String directory : config.getBinTestDir()) {
            includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
        }
    }
    return includes.toString();
}
```