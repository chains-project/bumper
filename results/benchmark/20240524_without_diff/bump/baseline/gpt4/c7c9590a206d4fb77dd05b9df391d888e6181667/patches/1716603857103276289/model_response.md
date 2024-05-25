```java
@Override
public void execute() throws MojoExecutionException {
    if (!canGenerateReport()) {
        getLog().info("Skipping SCoverage report generation");
        return;
    }

    try {
        File outputDir = outputDirectory;
        String outputName = getOutputName() + ".html";
        RenderingContext context = new RenderingContext(outputDir, outputName);
        Sink sink = new SiteRendererSink(context);
        Locale locale = Locale.getDefault();
        generate(sink, null, locale);
    } catch (MavenReportException e) {
        String prefix = "An error has occurred in " + getName(Locale.ENGLISH) + " report generation";
        throw new MojoExecutionException(prefix + ": " + e.getMessage(), e);
    }
}
```