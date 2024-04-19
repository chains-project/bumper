Here's a proposed patch for the failing client code:

```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

// ...

public class SCoverageReportMojo extends AbstractMojo {
    // ...

    @Override
    protected void renderDocument(Writer writer, SiteRenderingContext siteContext) throws MojoExecutionException {
        try (RenderingContext renderingContext = new RenderingContext()) {
            super.renderDocument(writer, renderingContext, siteContext);
        }
    }

    // ...
}
```

The patch creates a new `RenderingContext` instance using the available constructor, and then passes it to the `renderDocument` method. This change should fix the compilation error, as it no longer depends on the removed methods.