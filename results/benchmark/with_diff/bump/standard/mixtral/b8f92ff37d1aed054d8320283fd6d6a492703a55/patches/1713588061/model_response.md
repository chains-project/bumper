Here's the fixed version of the `getClassesLoc` method, using the new API:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.booterclient.ForkConfiguration surefireForkConfiguration = new org.apache.maven.plugin.surefire.booterclient.DefaultForkConfiguration(new org.apache.maven.plugin.surefire.booterclient.lazytestprovider.ClasspathSettings(new java.util.ArrayList<>(), new java.util.ArrayList<>(), new java.util.ArrayList<>()));
    org.apache.maven.plugin.surefire.booterclient.lazytestprovider.Commandline commandLine = surefireForkConfiguration.createCommandLine(new org.apache.maven.surefire.booter.SurefireBooterFactory.Surefirebooter30Configuration(), 0, testSrcFolder);
    org.apache.maven.plugin.surefire.booterclient.lazytestprovider.TestRequest testRequest = new org.apache.maven.plugin.surefire.booterclient.lazytestprovider.TestRequest();
    commandLine.addTestRequest(testRequest);
    org.apache.maven.plugin.surefire.booterclient.lazytestprovider.TestRequestResult testRequestResult = commandLine.execute();
    org.apache.maven.plugin.surefire.report.ReportEntry reportEntry = testRequestResult.getReportEntry();
    return reportEntry.getClasses();
}
```

This version of the method creates a new `DefaultForkConfiguration` instance and then uses the `createCommandLine` method to configure the command line for the new API.
The `TestRequest` instance is then added to the command line, and the `execute` method is called to run the tests.
Finally, the report entry is retrieved from the result, and the list of classes is returned.