```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        // ...
        try (Writer writer = getWriter()) {
            RenderingContext renderingContext = new RenderingContext();
            // ...
            renderer.renderDocument(writer, renderingContext, siteRenderingContext);
        }
        // ...
    }

    private Writer getWriter() {
        // ...
    }
}
```