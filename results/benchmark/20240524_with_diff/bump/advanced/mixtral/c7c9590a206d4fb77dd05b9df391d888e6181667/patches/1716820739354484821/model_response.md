Here's the patched version of the failing method:
```java
import org.apache.maven.doxia.siterenderer.RenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

import java.io.StringWriter;

// ...

protected void renderDocument(Writer writer, RenderingContext renderContext, SiteRenderingContext siteRenderingContext) throws IOException {
    StringWriter stringWriter = new StringWriter();
    SiteRendererSink sink = siteRenderingContext.createSiteRendererSink(renderContext);
    renderContext.setOutputName("target/site/output");

    try (Writer outputWriter = sink.getWriter(stringWriter)) {
        siteRenderingContext.getRenderer().renderDocument(outputWriter, renderContext, siteRenderingContext);
    }

    String output = stringWriter.toString();
    writer.write(output);
}
```
The patch creates a `SiteRendererSink` using the `siteRenderingContext` instead of using the deprecated constructor. Also, the `RenderingContext`'s `setOutputName` method is used to set the output name instead of using the deprecated `DoxiaDocumentRenderer` class.