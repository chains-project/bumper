```java
import java.util.Locale;
import java.util.Optional;

import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.reporting.MavenReportException;
import org.scoverage.plugin.RenderingContext;
import org.scoverage.plugin.SCoverageReportMojo;

public class SCoverageReportMojo extends SCoverageReportMojo {

  @Override
  public void execute() throws MojoExecutionException {
    if (!canGenerateReport()) {
      getLog().info("Skipping SCoverage report generation");
      return;
    }

    try {
      Optional<RenderingContext> renderingContext = getRenderingContext();
      if (renderingContext.isPresent()) {
        SiteRendererSink sink = new SiteRendererSink(renderingContext.get());
        Locale locale = Locale.getDefault();
        generate(sink, locale);
      } else {
        getLog().info("Skipping SCoverage report generation due to missing rendering context.");
      }
    } catch (MavenReportException e) {
      String prefix = ("An error has occurred in " + getName(Locale.ENGLISH)) + " report generation";
      throw new MojoExecutionException(prefix + ": " + e.getMessage(), e);
    }
  }

  private Optional<RenderingContext> getRenderingContext() {
    try {
      return Optional.of(new RenderingContext(outputDirectory, getOutputName() + ".html"));
    } catch (Exception e) {
      getLog().warn("Failed to create RenderingContext", e);
      return Optional.empty();
    }
  }
}
```