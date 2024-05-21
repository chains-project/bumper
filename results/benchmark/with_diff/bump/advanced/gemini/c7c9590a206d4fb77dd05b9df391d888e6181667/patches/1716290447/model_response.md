```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;

public class SCoverageReportMojo {

    public void generateReport(RenderingContext renderingContext) {
        // Use the RenderingContext to get the output name
        String outputName = renderingContext.getOutputName();
        // ...
    }

}
```