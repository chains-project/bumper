```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

public void renderDocument(java.io.Writer writer, RenderingContext renderingContext, org.apache.maven.doxia.siterenderer.SiteRenderingContext siteRenderingContext) {
  // Get the output name from the RenderingContext
  String outputName = renderingContext.getOutputName();

  // Use the output name to determine the file extension
  String fileExtension = outputName.substring(outputName.lastIndexOf(".") + 1);

  // Create a SiteRendererSink based on the file extension
  org.apache.maven.doxia.siterenderer.sink.SiteRendererSink sink = null;
  if ("html".equals(fileExtension)) {
    sink = new org.apache.maven.doxia.siterenderer.sink.HtmlSink(writer);
  } else if ("xml".equals(fileExtension)) {
    sink = new org.apache.maven.doxia.siterenderer.sink.XmlSink(writer);
  } else {
    throw new IllegalArgumentException("Unsupported file extension: " + fileExtension);
  }

  // Render the document using the SiteRendererSink
  siteRenderingContext.getRenderer().renderDocument(writer, renderingContext, siteRenderingContext);

  // Close the SiteRendererSink
  sink.close();
}
```