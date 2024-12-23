Here's the proposed patch for the failing client code:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.CommandlineParameters;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.SurefireLauncherFactory;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.TestSetFailedException;
import org.apache.maven.plugin.surefire.report.SimpleReportEntry;
import org.apache.maven.plugin.surefire.report.SurefireReportParser;
import org.apache.maven.plugin.surefire.report.TestSetReportEntry;
import org.apache.maven.plugin.surefire.util.TestsToRun;
import org.apache.maven.surefire.api.testset.TestSetFailedException2;
import org.apache.maven.surefire.api.testset.TestSetResult;
import org.apache.maven.surefire.api.testset.TestType;
import org.apache.maven.surefire.common.junit4.JUnit4Provider;
import org.apache.maven.surefire.report.ReportEntry;
import org.apache.maven.surefire.report.ReporterFactory;
import org.apache.maven.surefire.report.provider.UseFile;
import org.apache.maven.surefire.report.provider.UseFileBuilder;
import org.apache.maven.surefire.report.provider. surefire.ReportEntryImpl;
import org.apache.maven.surefire.suite.SurefireDataFileManager;
import org.apache.maven.surefire.testset.TestRequest;
import org.apache.maven.surefire.testset.TestSet;
import org.apache.maven.surefire.testset.TestTypeCount;
import org.apache.maven.surefire.util.TestsToRunImpl;
import org.apache.maven.surefire.util.ThreadSafeStack;
import org.apache.maven.surefire.util.TestsToRunImpl2;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Properties;
import java.util.Set;
import java.util.TreeSet;

import static java.util.Arrays.asList;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) throws IOException, TestSetFailedException {
    org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration defaultForkConfiguration = new org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration(new File("target/surefire-reports"), new Properties());
    Commandline commandLine = defaultForkConfiguration.createCommandLine(new StartupConfiguration(), 1, testSrcFolder);
    org.apache.maven.plugin.surefire.booterclient.SurefireBooterClientFactory surefireBooterClientFactory = new org.apache.maven.plugin.surefire.booterclient.SurefireBooterClientFactory();
    org.apache.maven.plugin.surefire.booterclient.SurefireBooterClient surefireBooterClient = surefireBooterClientFactory.createSurefireBooterClient(commandLine);
    TestsToRun testsToRun = new TestsToRunImpl2(asList(testSrcFolder));
    TestSetResult testSetResult = surefireBooterClient.run(testsToRun);
    SurefireReportParser surefireReportParser = new SurefireReportParser();
    Collection<ReportEntry> reportEntries = surefireReportParser.parseReportEntries(new File(testSetResult.getReportDirectory()));
    List<ReportEntry> reportEntriesSorted = new ArrayList<>(reportEntries);
    Collections.sort(reportEntriesSorted, new Comparator<ReportEntry>() {
        @Override
        public int compare(ReportEntry o1, ReportEntry o2) {
            return o1.getTestClass().compareTo(o2.getTestClass());
        }
    });
    List<String> classesLoc = new ArrayList<>();
    for (ReportEntry reportEntry : reportEntriesSorted) {
        classesLoc.add(reportEntry.getTestClass());
    }
    return classesLoc;
}
```

I replaced `DirectoryScanner` and `TestListResolver` with `DefaultForkConfiguration`, `SurefireBooterClientFactory`, `SurefireBooterClient`, `TestsToRun`, `TestSetResult`, `SurefireReportParser`, and `ReportEntry`. I also added necessary imports to make the code compile.