Here is a patch that you can apply to the failing method:

```java
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.Commandline;
import org.apache.maven.plugin.surefire.provider.AbstractSurefireProvider;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new AbstractSurefireProvider.TestListResolver() {
        @Override
        protected String getWildcard() {
            return "**/*.class";
        }
    }.getWildcard());
    return directoryScanner.scan().getClasses();
}
```

This patch creates an anonymous subclass of `AbstractSurefireProvider.TestListResolver` and overrides the `getWildcard()` method to return the string `"**/*.class"`, which should be a valid wildcard for scanning for class files. This should allow the `DirectoryScanner` to function correctly and avoid the "cannot find symbol" error.