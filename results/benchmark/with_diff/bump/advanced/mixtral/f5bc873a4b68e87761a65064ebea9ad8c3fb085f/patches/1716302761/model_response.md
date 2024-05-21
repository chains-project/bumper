Here's the proposed patch for the client code:
```java
import org.apache.maven.project.MavenProjectBuilder;
import org.apache.maven.project.ProjectBuilderConfiguration;
import org.apache.maven.project.ProjectBuildingException;

// ...

private MavenProject getMavenProject() throws ProjectBuildingException {
    ProjectBuilderConfiguration config = new ProjectBuilderConfiguration();
    MavenProjectBuilder builder = new MavenProjectBuilder();
    return builder.build(this.getBasedir(), this.getProject().getBasedir(), config);
}
```
In the new library version, the `MavenProject` class has been removed. Instead, you can use `MavenProjectBuilder` to create a `MavenProject`.