Here's the patched method:

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
        directoryScanner.setIncludes(new java.util.Arrays.asList("**/" + className + ".class"));
        directoryScanner.scan();
        if (!directoryScanner.getIncludedFiles().isEmpty()) {
            return true;
        }
    }
    for (java.lang.String dir : config.getBinTestDir()) {
        org.apache.maven.shared.utils.io.DirectoryScanner directoryScanner = new org.apache.maven.shared.utils.io.DirectoryScanner(new java.io.File(dir));
        directoryScanner.setIncludes(new java.util.Arrays.asList("**/" + className + ".class"));
        directoryScanner.scan();
        if (!directoryScanner.getIncludedFiles().isEmpty()) {
            return true;
        }
    }
    return false;
}
```

The main change is the usage of `org.apache.maven.shared.utils.io.DirectoryScanner` instead of `org.apache.maven.plugin.surefire.util.DirectoryScanner` and `directoryScanner.setIncludes()` instead of `directoryScanner.getClasses()`. This change resolves the issue with the removed `getWildcard()` method.