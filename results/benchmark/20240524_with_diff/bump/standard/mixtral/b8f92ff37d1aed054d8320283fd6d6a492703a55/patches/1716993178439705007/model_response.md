Here's the fixed `getClassesLoc` method:

```java
import org.apache.maven.plugin.surefire.booterclient.Commandline;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.CommandlineParameters;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.SurefireLauncher;
import org.apache.maven.plugin.surefire.booterclient.lazytestprovider.TestSetFailedException;
import org.apache.maven.surefire.api.testset.TestRequest;
import org.apache.maven.surefire.api.testset.TestSetFilter;
import org.apache.maven.surefire.api.util.DefaultScanResult;
import org.apache.maven.surefire.api.util.ScanResult;
import org.apache.maven.surefire.api.util.TestSetFailedException2;

import java.io.File;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

static List<String> getClassesLoc(File testSrcFolder) {
    TestSetFilter testSetFilter = new TestSetFilter() {
        @Override
        public List<String> getIncludes() {
            return Collections.singletonList("**/*.class");
        }

        @Override
        public List<String> getExcludes() {
            return Collections.emptyList();
        }
    };

    TestRequest testRequest = new TestRequest();
    testRequest.setTestClasses(testSetFilter);

    SurefireLauncher surefireLauncher = new SurefireLauncher();
    CommandlineParameters commandlineParameters = new CommandlineParameters();
    commandlineParameters.setTestClassesDirectory(testSrcFolder);
    commandlineParameters.setTestRequest(testRequest);

    Commandline commandline = surefireLauncher.createCommandLine(commandlineParameters);

    try {
        ScanResult scanResult = surefireLauncher.run(commandline);
        return Arrays.asList(scanResult.getIncludedClasses());
    } catch (TestSetFailedException2 e) {
        throw new RuntimeException("Failed to scan test classes", e);
    }
}
```

This updated method uses the `SurefireLauncher` class to scan the test classes in the `testSrcFolder`. It creates a `TestRequest` object with the specified `testSetFilter` and then uses the `SurefireLauncher` to create a `Commandline` instance. The `SurefireLauncher` is then used to run the tests and retrieve the scan result, from which the included class names are extracted.

This code should work with the updated library version, as it doesn't depend on the removed `TestListResolver` class or its `getWildcard` method.