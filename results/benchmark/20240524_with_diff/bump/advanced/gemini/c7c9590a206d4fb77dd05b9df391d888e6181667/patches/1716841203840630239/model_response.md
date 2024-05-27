```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

public class SCoverageReportMojo {

    public void execute() {
        SiteRenderingContext siteRenderingContext = new SiteRenderingContext();
        SiteRendererSink sink = new SiteRendererSink(siteRenderingContext);
        sink.head();
        sink.title();
        sink.text("SCoverage Report");
        sink.title_();
        sink.head_();
        sink.body();
        // ...
        sink.body_();
    }
}
```