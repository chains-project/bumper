```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext_For_Doxia;

public class SCoverageReportMojo {

    public void execute() {
        RenderingContext context = new RenderingContext_For_Doxia();
        // ...
    }
}
```