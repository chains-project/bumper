```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() {
        // ...
        RenderingContext renderingContext = new RenderingContext();
        renderingContext.setOutputName("scoverage-report.xml");
        // ...
    }

}
```