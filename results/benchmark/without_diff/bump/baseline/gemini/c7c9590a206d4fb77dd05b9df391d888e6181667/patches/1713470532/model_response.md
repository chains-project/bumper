```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.sink.Sink;

public class SCoverageReportMojo {
  public void execute() {
    // ...
    Sink sink = getSink();
    RenderingContext context = new RenderingContext(sink, getLocale());
    // ...
  }
}
```