```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.siterenderer.DocumentRenderer;
import org.apache.maven.doxia.siterenderer.RenderingContext;
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        // ...

        // Get the Doxia document renderer
        DocumentRenderer documentRenderer = getDoxiaDocumentRenderer();

        // Create a new RenderingContext
        RenderingContext renderingContext = documentRenderer.getRenderingContext();

        // Set the output name
        renderingContext.setOutputName("scoverage-report.html");

        // Render the document
        documentRenderer.renderDocument(writer, renderingContext, siteRenderingContext);

        // ...
    }

    private DocumentRenderer getDoxiaDocumentRenderer() {
        // ...

        // Create a new Doxia document renderer
        DocumentRenderer documentRenderer = new DoxiaDocumentRenderer(renderingContext);

        // ...

        return documentRenderer;
    }
}
```