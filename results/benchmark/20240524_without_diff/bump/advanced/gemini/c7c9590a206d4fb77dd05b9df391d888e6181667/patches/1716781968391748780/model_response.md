```java
@java.lang.Override
public void execute() throws org.apache.maven.plugin.MojoExecutionException {
    if (!canGenerateReport()) {
        getLog().info("Skipping SCoverage report generation");
        return;
    }
    try {
        org.apache.maven.reporting.MavenReportException e = new org.apache.maven.reporting.MavenReportException("An error has occurred in SCoverage report generation");
        throw new org.apache.maven.plugin.MojoExecutionException(e.getMessage(), e);
    }
}
```