```java
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;
import org.scoverage.plugin.ScoverageReportMojo;

import java.io.File;
import java.io.IOException;
import java.util.Locale;

public class ScoverageReportMojo extends ScoverageReportMojo {

    @Override
    public void execute() throws MojoExecutionException {
        if (!canGenerateReport()) {
            getLog().info("Skipping SCoverage report generation");
            return;
        }
        try {
            File scoverageReportFile = new File(outputDirectory, getOutputName() + ".html");
            SiteRendererSink sink = new SiteRendererSink(scoverageReportFile);
            Locale locale = Locale.getDefault();
            generate(sink, locale);
        } catch (IOException e) {
            String prefix = ("An error has occurred in " + getName(Locale.ENGLISH)) + " report generation";
            throw new MojoExecutionException(prefix + ": " + e.getMessage(), e);
        }
    }
}
```