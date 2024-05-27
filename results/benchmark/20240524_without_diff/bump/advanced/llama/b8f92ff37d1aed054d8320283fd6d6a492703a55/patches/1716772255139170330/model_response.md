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
        org.apache.maven.shared.utils.cli.StreamReader streamReader = new org.apache.maven.shared.utils.cli.StreamReader();
        java.io.FileSet fileSet = new java.io.FileSet(dir);
        fileSet.setIncludes(new java.lang.String[]{"**/*.class"});
        if (fileSet.getDirectoryScanner().scan().getIncludedFiles().length > 0) {
            for (java.lang.String file : fileSet.getDirectoryScanner().getIncludedFiles()) {
                if (className.equals(file.replace('/', '.').replace(".class", ""))) {
                    return true;
                }
            }
        }
    }
    for (java.lang.String dir : config.getBinTestDir()) {
        org.apache.maven.shared.utils.cli.StreamReader streamReader = new org.apache.maven.shared.utils.cli.StreamReader();
        java.io.FileSet fileSet = new java.io.FileSet(dir);
        fileSet.setIncludes(new java.lang.String[]{"**/*.class"});
        if (fileSet.getDirectoryScanner().scan().getIncludedFiles().length > 0) {
            for (java.lang.String file : fileSet.getDirectoryScanner().getIncludedFiles()) {
                if (className.equals(file.replace('/', '.').replace(".class", ""))) {
                    return true;
                }
            }
        }
    }
    return false;
}
```