```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;

public class SCoverageReportMojo {

    public void execute() {
        // ...
        SiteRendererSink sink = new SiteRendererSink(new RenderingContext() {
            @Override
            public String getOutputName() {
                return "scoverage-report";
            }
        });
        // ...
    }
}
```