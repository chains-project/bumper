```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        // ...
        Writer writer = null;
        SiteRenderingContext siteRenderingContext = null;
        try {
            // ...
            siteRenderingContext = new SiteRenderingContext();
            siteRenderingContext.setOutputName("scoverage-report.xml");
            // ...
            renderer.renderDocument(writer, siteRenderingContext, siteRenderingContext);
            // ...
        } finally {
            // ...
        }
    }
}
```