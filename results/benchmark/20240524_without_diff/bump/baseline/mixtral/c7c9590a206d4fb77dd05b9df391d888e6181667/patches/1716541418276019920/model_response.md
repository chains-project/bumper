Here's the proposed patch:
```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

// ...

@Override
protected void renderDocument(Writer writer, RenderingContext renderingContext, SiteRenderingContext siteRenderingContext) throws SiteRendererException {
    String outputName = renderingContext.getOutputName();
    // ... (rest of the method)
}
```
This patch updates the import statement and uses the new method `getOutputName()` from the updated `RenderingContext` class.