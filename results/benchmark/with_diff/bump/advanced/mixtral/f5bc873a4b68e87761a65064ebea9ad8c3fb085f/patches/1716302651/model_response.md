Here's the patched version of the failing method that should fix the error:
```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectConfigurator;
import org.apache.maven.project.ProjectBuildingException;

// ...

private MavenProject getMavenProject() throws ProjectBuildingException {
    ProjectBuilder projectBuilder = new ProjectBuilder();
    ProjectConfigurator projectConfigurator = new ProjectConfigurator();

    return projectBuilder.build(getBasedir(), getProject().getModel(), projectConfigurator).getProject();
}
```
In the new version of the library, the `MavenProject` class is no longer directly imported, but it can be obtained through the `ProjectBuilder` class.

The `getBasedir()` and `getProject()` methods should be available in the context where this code is used.

Please make sure to adjust them accordingly.