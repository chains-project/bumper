Here is the suggested patch for the failing client code:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booter.StartupConfiguration;
import org.apache.maven.plugin.surefire.util.DirectoryScanner;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    Commandline commandLine = new DefaultForkConfiguration().createCommandLine(new StartupConfiguration(), 0, testSrcFolder);
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, commandLine.getSetting("testListResolver").getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The changes made in this patch are:

* Importing the necessary classes for creating a Commandline object.
* Creating a Commandline object using the createCommandLine method of DefaultForkConfiguration.
* Getting the TestListResolver object from the Commandline object and using its getWildcard method to set the directory scanner.

This patch should resolve the "cannot find symbol" error caused by the removal of the getWildcard method from TestListResolver.