```java
import org.codehaus.plexus.classworlds.realm.ClassRealm;
import org.apache.maven.plugin.AbstractMojo;

public abstract class AbstractThemeMojo extends AbstractMojo {
    protected MavenProject getProject() {
        return (MavenProject) getContainer().lookup(MavenProject.class.getName());
    }

    private ClassRealm getContainer() {
        return (ClassRealm) getPluginContext().get("class.realm");
    }

    private java.util.Map getPluginContext() {
        return getPluginContextValue();
    }

    private java.util.Map getPluginContextValue() {
        return (java.util.Map) getContext().get("plugin.context");
    }

    private java.util.Map getContext() {
        return (java.util.Map) getMojoExecution().getContext();
    }

    private org.apache.maven.plugin.MojoExecution getMojoExecution() {
        return (org.apache.maven.plugin.MojoExecution) getPluginContext().get("mojo_execution");
    }
}
```