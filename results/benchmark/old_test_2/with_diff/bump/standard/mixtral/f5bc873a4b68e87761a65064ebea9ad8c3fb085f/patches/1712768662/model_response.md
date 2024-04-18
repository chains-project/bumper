Here is the proposed patch for the failing method in the client code:

```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectConfigurator;
import org.apache.maven.project.ProjectBuildingException;

//...

@Override
protected MavenProject readProject() throws MojoExecutionException {
    ProjectBuilder projectBuilder = (ProjectBuilder) lookup(ProjectBuilder.ROLE);
    File pomFile = new File(project.getBasedir(), project.getPomFile().getName());
    try {
        return projectBuilder.build(pomFile)
            .getProjects()
            .stream()
            .filter(p -> p.getArtifactId().equals(project.getArtifactId()))
            .findFirst()
            .orElseThrow(() -> new MojoExecutionException("Unable to find project for artifact id: " + project.getArtifactId()));
    } catch (ProjectBuildingException e) {
        throw new MojoExecutionException("Failed to build project", e);
    }
}
```

Note: The patch adds the following imports:

* `org.apache.maven.project.ProjectBuilder`
* `org.apache.maven.project.ProjectConfigurator`
* `org.apache.maven.project.ProjectBuildingException`

And it uses the `ProjectBuilder` to build the project instead of using the `MavenProjectBuilder` which has been removed.