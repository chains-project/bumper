```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        // ...

        SiteRenderingContext renderingContext = new SiteRenderingContext();
        SiteRendererSink sink = new SiteRendererSink(renderingContext);
        Writer writer = // ...

        // ...

        // Use the rendering context to get the output name
        String outputName = renderingContext.getOutputName();

        // ...
    }
}
```