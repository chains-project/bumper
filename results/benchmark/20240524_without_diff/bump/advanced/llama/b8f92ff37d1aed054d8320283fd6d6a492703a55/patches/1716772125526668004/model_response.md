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
        org.apache.maven.shared.utils.cli.StreamPumper pumper = new org.apache.maven.shared.utils.cli.StreamPumper();
        java.io.File directory = new java.io.File(dir);
        java.util.ArrayList<String> includes = new java.util.ArrayList<String>();
        includes.add("**/*.class");
        org.apache.maven.shared.utils.cli.Commandline cli = new org.apache.maven.shared.utils.cli.Commandline("find");
        cli.addArguments(new java.lang.String[] { directory.getAbsolutePath(), "-name", String.join(" -o -name ", includes) });
        pumper.streamCli(cli);
        java.util.List<String> classes = pumper.getOutputLines();
        for (java.lang.String clazz : classes) {
            if (clazz.endsWith(className + ".class")) {
                return true;
            }
        }
    }
    for (java.lang.String dir : config.getBinTestDir()) {
        org.apache.maven.shared.utils.cli.StreamPumper pumper = new org.apache.maven.shared.utils.cli.StreamPumper();
        java.io.File directory = new java.io.File(dir);
        java.util.ArrayList<String> includes = new java.util.ArrayList<String>();
        includes.add("**/*.class");
        org.apache.maven.shared.utils.cli.Commandline cli = new org.apache.maven.shared.utils.cli.Commandline("find");
        cli.addArguments(new java.lang.String[] { directory.getAbsolutePath(), "-name", String.join(" -o -name ", includes) });
        pumper.streamCli(cli);
        java.util.List<String> classes = pumper.getOutputLines();
        for (java.lang.String clazz : classes) {
            if (clazz.endsWith(className + ".class")) {
                return true;
            }
        }
    }
    return false;
}
```