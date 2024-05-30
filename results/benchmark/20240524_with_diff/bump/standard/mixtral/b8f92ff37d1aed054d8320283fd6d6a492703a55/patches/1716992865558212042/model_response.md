Here is a patch that you can apply to the failing code:
```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.CommandLineConfiguration;
import org.apache.maven.surefire.api.testset.TestListResolver;

import java.io.File;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    CommandLineConfiguration commandLineConfiguration = new CommandLineConfiguration();
    DefaultForkConfiguration defaultForkConfiguration = new DefaultForkConfiguration(commandLineConfiguration);
    TestListResolver testListResolver = new TestListResolver();
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, testListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```
The changes I made are:

* Import the necessary classes for `Commandline`, `DefaultForkConfiguration`, `CommandLineConfiguration`, and `TestListResolver`.
* Create instances of `CommandLineConfiguration` and `DefaultForkConfiguration`.
* Create an instance of `TestListResolver` and call the `getWildcard()` method on it.

These changes allow you to continue using the `DirectoryScanner` class and its `scan()` method, which returns a `TestClass` object that contains the list of classes in the specified directory.