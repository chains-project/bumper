```java
import org.apache.maven.doxia.siterenderer.RenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

public class SCoverageReportMojo {

    public void execute() {
        // ...
        RenderingContext renderingContext = new RenderingContext();
        SiteRendererSink sink = new SiteRendererSink(renderingContext);
        // ...
    }

}
```