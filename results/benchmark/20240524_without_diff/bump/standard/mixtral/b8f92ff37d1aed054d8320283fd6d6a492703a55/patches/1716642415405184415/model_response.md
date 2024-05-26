Here's the updated `computeJacocoIncludes` method that should resolve the error by using the static method `getWildcardPattern` from `org.apache.maven.surefire.api.util.SurefireReflectionUtils` to get the wildcard pattern instead of the removed `getWildcard` method from `TestListResolver`:

```java
protected java.lang.String computeJacocoIncludes() {
    java.lang.StringBuilder includes = new java.lang.StringBuilder();
    for (java.lang.String directory : config.getBinJavaDir()) {
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), getWildcardPattern());
        includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
    }
    if (config.isCoverTests()) {
        for (java.lang.String directory : config.getBinTestDir()) {
            org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), getWildcardPattern());
            includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
        }
    }
    return includes.toString();
}

private static String getWildcardPattern() {
    try {
        return (String) org.apache.maven.surefire.api.util.SurefireReflectionUtils.getInstance().getMethod(org.apache.maven.surefire.api.testset.TestListResolver.class, "getWildcard").invoke(null);
    } catch (Exception e) {
        throw new RuntimeException("Failed to get wildcard pattern", e);
    }
}
```

The `getWildcardPattern` method uses reflection to access the private `getWildcard` method from `TestListResolver`. This is not the most elegant solution, but it allows you to avoid updating the external dependency and still fix the error in the client code.