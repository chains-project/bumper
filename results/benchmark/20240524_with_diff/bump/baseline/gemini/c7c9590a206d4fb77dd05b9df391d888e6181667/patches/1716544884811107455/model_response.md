```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;

import java.io.Writer;

public class SCOverageReportMojo {

    public void renderDocument(Writer writer, SiteRenderingContext siteRenderingContext) {
        // Create a new RenderingContext object with the provided SiteRenderingContext.
        RenderingContext renderingContext = new RenderingContext(siteRenderingContext);

        // Call the renderDocument method of the DefaultSiteRenderer with the created RenderingContext.
        new DefaultSiteRenderer().renderDocument(writer, renderingContext, siteRenderingContext);
    }
}
```