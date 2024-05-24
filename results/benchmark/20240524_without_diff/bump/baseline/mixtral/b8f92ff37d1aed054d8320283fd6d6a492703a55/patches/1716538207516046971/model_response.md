Here's the fixed version of the `classToInclude` method:

```java
private boolean classToInclude(String className) {
    WildcardMatcher matcher = new WildcardMatcher("");
    // False if it matches an excludes pattern
    for (String pattern : config.getJacocoExcludes()) {
        matcher.setPattern(pattern);
        if (matcher.matches(className)) {
            return false;
        }
    }
    // True if it matches an includes pattern and doesn't match any excludes pattern
    for (String pattern : config.getJacocoIncludes()) {
        matcher.setPattern(pattern);
        if (matcher.matches(className)) {
            return true;
        }
    }

    Commandline commandLine = DefaultForkConfiguration.createCommandLine(StartupConfiguration.get(), 1, new File("target/surefire-reports"));
    DirectoryScanner directoryScanner = new DirectoryScanner(new File("target/classes"), commandLine);
    if (directoryScanner.scan().getClasses().contains(className)) {
        return true;
    }

    commandLine = DefaultForkConfiguration.createCommandLine(StartupConfiguration.get(), 1, new File("target/test-classes"));
    directoryScanner = new DirectoryScanner(new File("target/test-classes"), commandLine);
    if (directoryScanner.scan().getClasses().contains(className)) {
        return true;
    }

    return false;
}
```

The main change is the way the `DirectoryScanner` is initialized. Instead of using `TestListResolver.getWildcard()`, we create a `Commandline` instance using the `DefaultForkConfiguration.createCommandLine()` method, and then pass that to the `DirectoryScanner` constructor. This allows the code to work with the updated library version.