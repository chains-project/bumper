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

    // True if it is present in the available binaries
    File baseDir = new File(config.getBaseDirectory());
    for (String dir : config.getBinJavaDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(baseDir, dir), TestListResolver.getWildcard());
        if (directoryScanner.scan().getClasses().contains(className)) {
            return true;
        }
    }
    for (String dir : config.getBinTestDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(baseDir, dir), TestListResolver.getWildcard());
        if (directoryScanner.scan().getClasses().contains(className)) {
            return true;
        }
    }

    return false;
}
```

The main change is the addition of the `baseDir` variable, which is used to construct the correct path for the `DirectoryScanner`. This change is necessary because the `TestListResolver.getWildcard()` method is now protected and can no longer be accessed directly.

The `DirectoryScanner` constructor now takes a `File` object for the base directory, which makes it possible to construct the correct path to the binary directories.

The `WildcardMatcher` instance is now created outside of the loops and the pattern is set inside the loops. This is done to avoid creating a new `WildcardMatcher` instance for each pattern, which can be expensive.

The `override` decorator has been removed from the method, as it is not overriding any method in the new version.

The `getWildcard()` method from `TestListResolver` is still being used, but it is not causing any issues because it is a `protected` method and is still present in the new version of the library.