```java
@java.lang.Override
public void execute() throws org.apache.maven.plugin.MojoExecutionException {
    if (!canGenerateReport()) {
        getLog().info("Skipping SCoverage report generation");
        return;
    }
    try {
        org.apache.maven.doxia.siterenderer.RenderingContext context = new org.apache.maven.doxia.siterenderer.RenderingContext(outputDirectory, getOutputName() + ".html");
        org.apache.maven.doxia.siterenderer.SiteRenderingContext siteContext = new org.apache.maven.doxia.siterenderer.SiteRenderingContext(outputDirectory, getOutputName() + ".html");
        org.apache.maven.doxia.siterenderer.Renderer renderer = new org.apache.maven.doxia.siterenderer.Renderer();
        java.util.Locale locale = java.util.Locale.getDefault();
        org.apache.maven.doxia.siterenderer.DocumentContent documentContent = new org.apache.maven.doxia.siterenderer.DocumentContent();
        org.apache.maven.doxia.siterenderer.RenderingContext renderingContext = renderer.createContextForTemplate(outputDirectory, documentContent, new java.util.HashMap(), new org.apache.maven.doxia.site.decoration.DecorationModel(), getOutputName() + ".html", locale);
        org.apache.maven.doxia.siterenderer.SiteRendererSink sink = new org.apache.maven.doxia.siterenderer.SiteRendererSink(renderingContext);
        generate(sink, locale);
    } catch (org.apache.maven.reporting.MavenReportException e) {
        java.lang.String prefix = ("An error has occurred in " + getName(java.util.Locale.ENGLISH)) + " report generation";
        throw new org.apache.maven.plugin.MojoExecutionException((prefix + ": ") + e.getMessage(), e);
    }
}
```