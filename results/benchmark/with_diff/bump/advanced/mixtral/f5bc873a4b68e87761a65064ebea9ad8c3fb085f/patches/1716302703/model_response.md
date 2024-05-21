Here's a patched version of the failing method that should fix the error:
```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectConfigurator;
import org.apache.maven.project.ProjectBuildingException;

// ...

private MavenProject getMavenProject() throws ProjectBuildingException {
    ProjectBuilder projectBuilder = new ProjectBuilder();
    ProjectConfigurator projectConfigurator = new ProjectConfigurator();

    return projectBuilder.build(getModel(), projectConfigurator).getProject();
}
```
In the new library version, the `MavenProject` class is no longer directly available under the `org.apache.maven.project` package. Instead, it's now available under the `org.apache.maven` package.

The new `ProjectBuilder` and `ProjectConfigurator` classes are available under the `org.apache.maven.project` package.

With these changes, the code should now be able to build successfully.