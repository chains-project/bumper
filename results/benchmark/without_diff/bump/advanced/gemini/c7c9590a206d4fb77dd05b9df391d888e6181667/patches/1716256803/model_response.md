```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.sink.Sink;

public class SCoverageReportMojo {

    private RenderingContext context;

    public void execute() {
        Sink sink = context.getSink();
        // ...
    }
}
```