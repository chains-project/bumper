```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;

public class SCoverageReportMojo {

  public void execute() {
    // ...
  }

  private RenderingContext createRenderingContext() {
    // ...
    return new RenderingContext();
  }

  private void renderDocument(Writer writer, RenderingContext context, SiteRenderingContext siteContext) {
    // ...
  }
}
```