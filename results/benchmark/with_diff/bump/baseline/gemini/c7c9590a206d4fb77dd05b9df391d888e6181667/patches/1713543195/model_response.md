```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        try (Writer writer = getWriter()) {
            RenderingContext renderingContext = new RenderingContext();
            renderingContext.setOutputName("scoverage-report.xml");

            SiteRenderingContext siteRenderingContext = new SiteRenderingContext();
            siteRenderingContext.setGenerating("scoverage-report");

            getSiteRenderer().renderDocument(writer, renderingContext, siteRenderingContext);
        } catch (Exception e) {
            getLog().error("Error generating Scoverage report", e);
        }
    }

    private Writer getWriter() {
        // ...
    }

    private DoxiaSiteRenderer getSiteRenderer() {
        // ...
    }
}
```