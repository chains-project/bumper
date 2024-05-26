The library has removed the `org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext` class, so you cannot import it anymore. Based on the library changes, it seems like the `RenderingContext` class has been moved to `org.apache.maven.doxia.siterenderer.RenderingContext`. Here is the updated import statement:

```java
import org.apache.maven.doxia.siterenderer.RenderingContext;
```