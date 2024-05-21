Here's the proposed patch for the client code:
```java
import org.apache.maven.project.MavenProjectBuilder;
import org.apache.maven.project.ProjectBuilderConfiguration;
import org.apache.maven.project.ProjectBuildingException;

// ...

private MavenProject getMavenProject(String projectPath) throws ProjectBuildingException {
    ProjectBuilderConfiguration config = new ProjectBuilderConfiguration();
    MavenProjectBuilder builder = new MavenProjectBuilder();
    return builder.build(new File(projectPath), config).getProject();
}
```
In the updated library version, the `MavenProject` class is no longer directly accessible. Instead, you can use the `MavenProjectBuilder` class to build a `MavenProject` instance. This patch demonstrates how to use the new `MavenProjectBuilder` class to create a `MavenProject` instance.