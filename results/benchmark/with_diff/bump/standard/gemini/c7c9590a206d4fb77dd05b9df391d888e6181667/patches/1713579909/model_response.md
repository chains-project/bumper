```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() throws Exception {
        // ...
        RenderingContext renderingContext = new RenderingContext();
        // ...
        writer.write(renderingContext.getOutputName());
        // ...
    }
}
```