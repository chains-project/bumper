```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.DefaultProjectBuildingRequest;

public abstract class AbstractThemeMojo {
    protected MavenSession session;

    public abstract void execute();

    public void setSession(MavenSession session) {
        this.session = session;
    }

    public MavenSession getSession() {
        return session;
    }

    public void execute() {
        DefaultProjectBuildingRequest request = new DefaultProjectBuildingRequest();
        // rest of the method implementation
    }
}
```