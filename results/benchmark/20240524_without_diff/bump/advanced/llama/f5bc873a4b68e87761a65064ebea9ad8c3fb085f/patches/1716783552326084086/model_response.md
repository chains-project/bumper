```java
import org.codehaus.plexus.util.xml.Xpp3Dom;
import org.apache.maven.plugin.AbstractMojo;

public org.apache.maven.execution.MavenSession getProject() {
    return ((AbstractMojo) this).getPluginContext().getContext().getMavenSession();
}
```