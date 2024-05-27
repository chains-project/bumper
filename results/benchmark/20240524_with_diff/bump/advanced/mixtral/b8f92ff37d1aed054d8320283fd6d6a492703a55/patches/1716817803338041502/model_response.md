Here's the proposed patch to fix the error in the client code:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProviderFactory;
import org.apache.maven.surefire.api.testset.TestListResolver;

import java.io.File;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    File reportsDir = new DefaultForkConfiguration().getReportsDirectory();
    Commandline commandLine = LazyTestProviderFactory.createCommandLine(new DefaultForkConfiguration(), 1, reportsDir);
    TestListResolver testListResolver = TestListResolver.getWildcard();
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, testListResolver);
    return directoryScanner.scan().getClasses();
}
```

The changes made include:

* Importing the necessary classes for creating a `Commandline` object and getting the `TestListResolver` object.
* Creating a `Commandline` object using the `LazyTestProviderFactory` class.
* Using the `getReportsDirectory()` method from `DefaultForkConfiguration` to create the `reportsDir` object.
* Replacing the deprecated `OutputStreamFlushableCommandline` with `Commandline`.