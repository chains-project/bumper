Here's the updated `computeJacocoIncludes` method that should resolve the error:

```java
protected java.lang.String computeJacocoIncludes() {
    java.lang.StringBuilder includes = new java.lang.StringBuilder();
    for (java.lang.String directory : config.getBinJavaDir()) {
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), new org.apache.maven.surefire.api.testset.TestListResolver() {
            @Override
            public java.lang.String getWildcard() {
                return "**/*.class";
            }
        }.getWildcard());
        includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
    }
    if (config.isCoverTests()) {
        for (java.lang.String directory : config.getBinTestDir()) {
            org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(directory), new org.apache.maven.surefire.api.testset.TestListResolver() {
                @Override
                public java.lang.String getWildcard() {
                    return "**/*.class";
                }
            }.getWildcard());
            includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce(( x, y) -> (x + ":") + y).orElse(""));
        }
    }
    return includes.toString();
}
```

The change is to create an anonymous class extending `TestListResolver` and override the `getWildcard` method to return "**\/*.class" as the wildcard. This is needed because the `getWildcard` method is no longer available in the updated library version.