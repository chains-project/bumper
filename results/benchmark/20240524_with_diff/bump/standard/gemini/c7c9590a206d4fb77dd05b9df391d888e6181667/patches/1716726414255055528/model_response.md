```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;

public class SCoverageReportMojo {

    public void execute() {
        RenderingContext renderingContext = new RenderingContext();
        renderingContext.setOutputName("scoverage-report.xml");
        // rest of the code remains unchanged
    }
}
```