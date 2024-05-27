```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

public class SCoverageReportMojo {

    public void execute() {
        RenderingContext context = new RenderingContext();
        context.setOutputName("scoverage-report.xml");
    }
}
```