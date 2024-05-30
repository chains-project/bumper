Here's the patched version of the failing method:
```java
import org.apache.maven.doxia.siterenderer.RenderingContext;
import java.io.StringWriter;

// ...

private void renderSite(SiteRenderingContext siteContext)
        throws SiteRendererException, IOException {
    StringWriter writer = new StringWriter();
    RenderingContext renderingContext = siteContext.createRenderingContext(siteContext);
    siteRenderer.renderDocument(writer, renderingContext, siteContext);
    // ...
}
```
In this patch, I replaced the import statement to use the new location of the `RenderingContext` class. I also changed the creation of the rendering context to use the new method `SiteRenderingContext.createRenderingContext(SiteRenderingContext)`.