```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        // ...
        try (Writer writer = getWriter()) {
            RenderingContext renderingContext = new RenderingContext();
            renderingContext.setOutputName("scoverage-report.xml");
            getSiteRenderer().renderDocument(writer, renderingContext, getSiteRenderingContext());
        }
        // ...
    }

    // ...

    private Writer getWriter() {
        // ...
    }

    private SiteRenderingContext getSiteRenderingContext() {
        // ...
    }

}
```