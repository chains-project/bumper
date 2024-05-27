Here's the updated method with the required changes:

```java
private boolean classToInclude(java.lang.String className) {
    // False if it matches an excludes pattern
    for (java.lang.String pattern : config.getJacocoExcludes()) {
        org.jacoco.core.runtime.WildcardMatcher matcher = new org.jacoco.core.runtime.WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return false;
        }
    }
    // True if it matches an includes pattern and doesn't match any excludes pattern
    for (java.lang.String pattern : config.getJacocoIncludes()) {
        org.jacoco.core.runtime.WildcardMatcher matcher = new org.jacoco.core.runtime.WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return true;
        }
    }
    // True if it is present in the available binaries
    for (java.lang.String dir : config.getBinJavaDir()) {
        org.apache.maven.shared.utils.io.DirectoryScanner directoryScanner = new org.apache.maven.shared.utils.io.DirectoryScanner(new java.io.File(dir));
        directoryScanner.addDefaultExcludes();
        directoryScanner.addDefaultExcludes();
        directoryScanner.setIncludes(new java.util.ArrayList<>(Arrays.asList("**/" + className)));
        directoryScanner.scan();
        if (!directoryScanner.getIncludedFiles().isEmpty()) {
            return true;
        }
    }
    for (java.lang.String dir : config.getBinTestDir()) {
        org.apache.maven.shared.utils.io.DirectoryScanner directoryScanner = new org.apache.maven.shared.utils.io.DirectoryScanner(new java.io.File(dir));
        directoryScanner.addDefaultExcludes();
        directoryScanner.addDefaultExcludes();
        directoryScanner.setIncludes(new java.util.ArrayList<>(Arrays.asList("**/" + className)));
        directoryScanner.scan();
        if (!directoryScanner.getIncludedFiles().isEmpty()) {
            return true;
        }
    }
    return false;
}
```

The major change is the replacement of `TestListResolver.getWildcard()` with an empty ArrayList. This change is due to the fact that the `TestListResolver` class no longer has the `getWildcard()` method. Instead, the `DirectoryScanner` class is now used with default excludes and the desired class name as the include.