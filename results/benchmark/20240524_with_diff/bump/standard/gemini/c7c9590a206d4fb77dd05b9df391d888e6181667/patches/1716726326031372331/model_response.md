```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;

import java.io.IOException;

public class SCoverageReportMojo {

    public void execute() throws IOException {
        // ...
        RenderingContext renderingContext = new RenderingContext();
        // ...
        renderingContext.setOutputName("scoverage-report.xml");
        // ...
    }

}
```