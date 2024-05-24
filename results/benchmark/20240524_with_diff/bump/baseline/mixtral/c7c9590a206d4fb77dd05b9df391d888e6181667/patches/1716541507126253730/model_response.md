Here's the proposed patch:
```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

// ...

public class SCoverageReportMojo {
    // ...

    @Override
    protected void renderDocument(Writer writer, RenderingContext renderingContext, SiteRenderingContext siteRenderingContext) throws IOException {
        String outputName = renderingContext.getOutputName();
        // ... use 'outputName' as needed ...

        // ... rest of the method ...
    }
}
```
This patch updates the import statement and uses the new method `getOutputName()` from the `RenderingContext` class.