```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;

import java.io.IOException;
import java.io.Writer;

public class SCoverageReportMojo {

    public void execute() throws IOException {
        // ...
        RenderingContext renderingContext = new RenderingContext();
        // ...
        Writer writer = // ...
        renderingContext.setOutputName("scoverage-report.xml");
        // ...
    }
}
```