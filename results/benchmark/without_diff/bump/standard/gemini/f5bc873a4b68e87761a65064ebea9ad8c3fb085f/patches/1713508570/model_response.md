```java
import org.apache.myfaces.tobago.maven.plugin.AbstractThemeMojo;
import org.apache.maven.project.MavenProject;

public class AbstractThemeMojo extends AbstractThemeMojo {

    public MavenProject getProject() {
        return project;
    }

}
```