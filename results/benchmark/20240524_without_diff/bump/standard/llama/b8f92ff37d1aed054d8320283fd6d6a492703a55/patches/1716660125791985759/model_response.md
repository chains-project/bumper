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
        org.apache.maven.shared.utils.cli.Commandline wildcard = new org.apache.maven.shared.utils.cli.Commandline();
        wildcard.createArg().setValue("**/*.class");
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(dir), wildcard);
        if (directoryScanner.scan().getIncludedFiles().stream().anyMatch(f -> f.endsWith(className.replace('.', '/') + ".class"))) {
            return true;
        }
    }
    for (java.lang.String dir : config.getBinTestDir()) {
        org.apache.maven.shared.utils.cli.Commandline wildcard = new org.apache.maven.shared.utils.cli.Commandline();
        wildcard.createArg().setValue("**/*.class");
        org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(new java.io.File(dir), wildcard);
        if (directoryScanner.scan().getIncludedFiles().stream().anyMatch(f -> f.endsWith(className.replace('.', '/') + ".class"))) {
            return true;
        }
    }
    return false;
}
```