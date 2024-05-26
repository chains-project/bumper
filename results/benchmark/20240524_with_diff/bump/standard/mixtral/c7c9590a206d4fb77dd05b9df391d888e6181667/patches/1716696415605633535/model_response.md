Here's the proposed patch:
```java
import org.apache.maven.doxia.siterenderer.RenderingContext;

// ...

RenderingContext renderingContext = siteRenderer.getRenderingContext();
String outputName = renderingContext.getOutputName();
```
Explanation:
Since the `RenderingContext` class is still available, we can use it to get the output name. The `getOutputName()` method was added in the new version, so we can use it to get the output name.