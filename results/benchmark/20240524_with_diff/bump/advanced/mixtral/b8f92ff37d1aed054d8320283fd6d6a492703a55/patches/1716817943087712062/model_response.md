Here is a possible patch for the code you provided:
```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.LazyTestProvider;
import org.apache.maven.plugin.surefire.common.junit4.JUnit4Provider;
import org.apache.maven.plugin.surefire.report.ReportEntry;
import org.apache.maven.plugin.surefire.report.ReportEntryFactory;
import org.apache.maven.plugin.surefire.report.SimpleReportEntry;
import org.apache.maven.plugin.surefire.report.SurefireReportGenerator;
import org.apache.maven.plugin.surefire.report.provider.SurefireReportProvider;
import org.apache.maven.plugin.surefire.report.provider.SurefireReportProviderFactory;
import org.apache.maven.plugin.surefire.util.DefaultScanResult;
import org.apache.maven.plugin.surefire.util.ScanResult;
import org.apache.maven.surefire.api.testset.TestRequest;
import org.apache.maven.surefire.api.testset.TestSetFailedException;
import org.apache.maven.surefire.booter.ForkMode;
import org.apache.maven.surefire.booter.ForkStarter;
import org.apache.maven.surefire.booter.ProviderParameter;
import org.apache.maven.surefire.booter.StartupConfiguration;
import org.apache.maven.surefire.common.junit.JUnit4ProviderFactory;
import org.apache.maven.surefire.common.junit.JUnit4TestChecker;
import org.apache.maven.surefire.common.junit.JUnit4TestSet;
import org.apache.maven.surefire.common.junit.TestSetFailedExceptionTranslator;
import org.apache.maven.surefire.common.util.ClasspathUtils;
import org.apache.maven.surefire.junitcore.JUnitCoreProvider;
import org.apache.maven.surefire.junitcore.JUnitCoreProviderFactory;
import org.apache.maven.surefire.provider.AbstractProvider;
import org.apache.maven.surefire.provider.ProviderParameters;
import org.apache.maven.surefire.provider.ProviderParametersBuilder;
import org.apache.maven.surefire.report.ReporterConfiguration;
import org.apache.maven.surefire.report.ReporterFactory;
import org.apache.maven.surefire.report.ReporterFactoryFactory;
import org.apache.maven.surefire.report.SimpleReporterConfiguration;
import org.apache.maven.surefire.shared.lang3.SystemStreamLog;
import org.apache.maven.surefire.testset.TestRequestFactory;
import org.apache.maven.surefire.testset.TestSetFactory;
import org.apache.maven.surefire.testset.TestSetFactoryFactory;
import org.apache.maven.surefire.util.ReflectionUtils;
import org.apache.maven.surefire.util.TestsToRun;
import org.apache.maven.surefire.util.TestsToRunFactory;
import org.apache.maven.surefire.util.TestsToRunFactoryFactory;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.Collectors;

static List<String> getClassesLoc(File testSrcFolder) {
    DefaultForkConfiguration forConfig = new DefaultForkConfiguration(testSrcFolder);
    Commandline commandLine = forConfig.createCommandLine(new StartupConfiguration(), ForkMode.perClass.getValue(), testSrcFolder);
    LazyTestProvider testProvider = new JUnit4Provider();
    ScanResult scanResult = testProvider.scan(commandLine);
    return Arrays.stream(scanResult.getIncludes())
        .map(s -> s.substring(0, s.length() - 4))
        .collect(Collectors.toList());
}
```
The main changes I made are:

* I replaced the `DirectoryScanner` class with a `DefaultForkConfiguration` object, which is a more appropriate way to scan a directory for tests in Surefire.
* I used the `createCommandLine` method of `DefaultForkConfiguration` to create a `Commandline` object, which represents the command line that will be executed to run the tests.
* I used the `scan` method of `JUnit4Provider` (which is a `LazyTestProvider`) to scan the directory specified in the `Commandline` object, and get a list of includes (i.e., the classes that match the wildcard pattern).
* I then used the `Arrays.stream` method to convert the array of includes to a list of strings, by removing the last 4 characters (i.e., the `.class` extension) from each include.

Note that this patch may not be the only possible solution, and it may not be the best solution depending on your specific use case. You may need to adapt it to your needs.