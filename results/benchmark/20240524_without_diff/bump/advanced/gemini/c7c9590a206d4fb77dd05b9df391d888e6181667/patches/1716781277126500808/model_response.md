```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.sink.Sink;

public class SCoverageReportMojo {

    private Sink sink;

    public void execute() {
        RenderingContext context = new RenderingContext(sink);
        // ...
    }
}
```