```java
import org.apache.maven.doxia.siterenderer.RenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

public class SCoverageReportMojo {

    public void execute() {
        // ...

        RenderingContext context = new RenderingContext();
        SiteRendererSink sink = new SiteRendererSink(context);

        // ...

        context.setOutputName("scoverage-report.xml");

        // ...
    }
}
```