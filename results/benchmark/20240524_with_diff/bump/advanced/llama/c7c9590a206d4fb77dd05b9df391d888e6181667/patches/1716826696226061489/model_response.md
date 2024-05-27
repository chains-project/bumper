```java
@java.lang.Override
public void execute() throws org.apache.maven.plugin.MojoExecutionException {
    if (!canGenerateReport()) {
        getLog().info("Skipping SCoverage report generation");
        return;
    }
    try {
        org.apache.maven.doxia.siterenderer.DefaultSiteRenderer renderer = new org.apache.maven.doxia.siterenderer.DefaultSiteRenderer();
        java.io.File outputDirectoryAsFile = new java.io.File(outputDirectory.getAbsolutePath());
        java.util.Map<String, String> emptyMap = new java.util.HashMap<>();
        org.apache.maven.doxia.siterenderer.SiteRenderingContext context = renderer.createContextForSkin(outputDirectoryAsFile, emptyMap, null, getOutputName() + ".html", java.util.Locale.getDefault());
        org.apache.maven.doxia.siterenderer.sink.SiteRendererSink sink = new org.apache.maven.doxia.siterenderer.sink.SiteRendererSink(context);
        generate(sink, java.util.Locale.getDefault());
    } catch (org.apache.maven.reporting.MavenReportException e) {
        java.lang.String prefix = ("An error has occurred in " + getName(java.util.Locale.ENGLISH)) + " report generation";
        throw new org.apache.maven.plugin.MojoExecutionException((prefix + ": ") + e.getMessage(), e);
    }
}
```