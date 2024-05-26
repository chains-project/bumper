```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

public class SCoverageReportMojo {

    public void execute() {
        // ...

        SiteRenderingContext renderingContext = new SiteRenderingContext();
        SiteRendererSink sink = new SiteRendererSink(renderingContext);
        sink.head();
        sink.title();
        sink.text("Scoverage Report");
        sink.title_();
        sink.head_();

        // ...
    }
}
```