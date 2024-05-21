Here's the proposed patch:
```java
import org.apache.maven.project.MavenProjectBuilder;
import org.apache.maven.project.ProjectBuilderConfiguration;
import org.apache.maven.project.ProjectBuildingException;

// ...

@Parameter
private MavenProjectBuilder projectBuilder;

// ...

private MavenProject getMavenProject(File pomFile) throws ProjectBuildingException {
    ProjectBuilderConfiguration config = new ProjectBuilderConfiguration();
    return projectBuilder.build(pomFile, config).getProject();
}
```
Explanation:
The error message indicates that the `org.apache.maven.project.MavenProject` class is not found, which was removed in the new library version. Instead, the `MavenProjectBuilder` class can be used to create a `MavenProject` instance. The `getMavenProject` method is updated accordingly.