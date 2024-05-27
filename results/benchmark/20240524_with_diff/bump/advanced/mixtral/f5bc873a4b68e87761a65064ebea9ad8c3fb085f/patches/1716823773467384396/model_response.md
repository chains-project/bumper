Here's the proposed patch for the failing method:
```java
import org.apache.maven.project.MavenProjectBuilder;
import org.apache.maven.project.ProjectBuilderConfiguration;
import org.apache.maven.project.ProjectBuildingRequest;

...

MavenProject mavenProject = mavenProjectBuilder
    .buildFromRepository(
        pomModel,
        new ProjectBuildingRequest()
            .forProject(new File(projectDirectory))
            .setProjectBuilderConfiguration(new ProjectBuilderConfiguration())
    )
    .getProject();
```
In this patch, I replaced the `MavenProject` import with `MavenProjectBuilder` and added the necessary imports for `ProjectBuilderConfiguration` and `ProjectBuildingRequest`. I then used the `MavenProjectBuilder` to build the `MavenProject` by specifying a `ProjectBuildingRequest` and a `ProjectBuilderConfiguration`.