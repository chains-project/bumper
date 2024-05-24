Here is a possible patch for the failing client code:
```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

// ...

public class SCoverageReportMojo {

    // ...

    @Override
    protected void executeReport(Locale locale) throws MojoExecutionException {
        // ...
        RenderingContext renderingContext = new RenderingContext();
        // ...
    }

    // ...

}
```
The patch creates a new instance of `RenderingContext` using its default constructor, which is still available in the new library version. This should fix the error.