```java
import org.apache.maven.plugin.Mojo;
import org.apache.maven.project.MavenProject;

public abstract class AbstractThemeMojo extends Mojo {

    protected MavenProject project;

    public void setProject(MavenProject project) {
        this.project = project;
    }

}
```