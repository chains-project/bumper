```java
import org.apache.maven.project.MavenProject;

public class AbstractThemeMojo {

    private MavenProject project;

    public AbstractThemeMojo(MavenProject project) {
        this.project = project;
    }

    public MavenProject getProject() {
        return project;
    }

    public void setProject(MavenProject project) {
        this.project = project;
    }
}
```