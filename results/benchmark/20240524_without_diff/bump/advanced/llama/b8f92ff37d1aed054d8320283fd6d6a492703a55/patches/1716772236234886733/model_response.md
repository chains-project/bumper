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
        org.apache.maven.shared.utils.io.FileUtils fileUtils = new org.apache.maven.shared.utils.io.FileUtils();
        java.io.File directory = new java.io.File(dir);
        java.lang.String[] files = fileUtils.getFiles(directory, "**/*.class");
        for (java.lang.String file : files) {
            java.lang.String clazz = file.replace(directory.getAbsolutePath() + java.io.File.separator, "").replace(".class", "").replace(java.io.File.separator, ".");
            if (clazz.equals(className)) {
                return true;
            }
        }
    }
    for (java.lang.String dir : config.getBinTestDir()) {
        org.apache.maven.shared.utils.io.FileUtils fileUtils = new org.apache.maven.shared.utils.io.FileUtils();
        java.io.File directory = new java.io.File(dir);
        java.lang.String[] files = fileUtils.getFiles(directory, "**/*.class");
        for (java.lang.String file : files) {
            java.lang.String clazz = file.replace(directory.getAbsolutePath() + java.io.File.separator, "").replace(".class", "").replace(java.io.File.separator, ".");
            if (clazz.equals(className)) {
                return true;
            }
        }
    }
    return false;
}
```