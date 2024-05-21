```java
import org.apache.maven.doxia.siterenderer.SiteRenderingContext;
import org.apache.maven.doxia.siterenderer.RenderingContext;

public class SCoverageReportMojo {

    public void execute() {
        RenderingContext renderingContext = new RenderingContext();
        renderingContext.setOutputName("scoverage-report.xml");
        SiteRenderingContext siteRenderingContext = new SiteRenderingContext();
        siteRenderingContext.setRenderingContext(renderingContext);
        // ...
    }
}
```