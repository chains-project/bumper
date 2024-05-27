```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        // ...
        RenderingContext renderingContext = new RenderingContext();
        renderingContext.setOutputName("scoverage-report.xml");
        SiteRendererSink sink = new SiteRendererSink(renderingContext);
        // ...
    }

}
```