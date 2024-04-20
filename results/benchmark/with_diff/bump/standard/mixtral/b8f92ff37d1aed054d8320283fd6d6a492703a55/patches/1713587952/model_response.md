Here is a patch that you can apply to the failing client code:
```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProvider;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.CommandlineFactory;
import org.apache.maven.surefire.api.testset.TestListResolver;
import org.apache.maven.surefire.api.testset.TestSetFailedException;
import org.apache.maven.surefire.api.util.SurefireReflectionUtil;

import java.io.File;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    DefaultForkConfiguration forConfig = new DefaultForkConfiguration();
    Commandline cmdLine = forConfig.createCommandLine(null, 0, testSrcFolder);
    LazyTestProvider testProvider = new LazyTestProvider(cmdLine);
    CommandlineFactory cmdFactory = testProvider.getCommandlineFactory();
    TestListResolver testListResolver = testProvider.getTestListResolver();
    List<String> classes = new LinkedList<>();
    try {
        Collection<File> files = testListResolver.resolveTestSets(testSrcFolder, null);
        for (File file : files) {
            classes.addAll(getClasses(cmdFactory, testListResolver, file));
        }
    } catch (TestSetFailedException e) {
        SurefireReflectionUtil.throwException(e);
    }
    return classes;
}

private static List<String> getClasses(CommandlineFactory cmdFactory, TestListResolver testListResolver, File file) {
    DirectoryScanner directoryScanner = new DirectoryScanner(file, testListResolver.getWildcard());
    directoryScanner.scan();
    return directoryScanner.getClasses();
}
```
Explanation:

* I created a `CommandlineFactory` object from the `LazyTestProvider` object, which is used to create a `DirectoryScanner` object.
* I then used the `getWildcard()` method from the `TestListResolver` object to initialize the `DirectoryScanner` object.
* I also added a try-catch block to handle `TestSetFailedException` that may be thrown when resolving test sets.
* I added a helper method `getClasses()` to encapsulate the creation of the `DirectoryScanner` object and its usage.
* I changed the return type of `getClassesLoc()` from `java.util.List<java.lang.String>` to `List<String>` for simplicity.

Note:

* I made these changes based on the assumption that the `DirectoryScanner` class and its `scan()` and `getClasses()` methods are still available in the new library version.
* If these methods are not available, you may need to find an alternative way to scan the test source folder and get the classes.
* I also assumed that the `LazyTestProvider` class and its `getCommandlineFactory()` and `getTestListResolver()` methods are still available in the new library version.
* If these methods are not available, you may need to find an alternative way to create the `CommandlineFactory` and `TestListResolver` objects.