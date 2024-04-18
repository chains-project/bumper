Here is a patched version of the failing method that uses the `MavenSession` class to get the `MavenProject`:

```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.ProjectBuilder;
import org.apache.maven.project.ProjectBuildingException;

// ...

@Override
protected MavenProject getProject(MavenSession session) throws MojoExecutionException {
    ProjectBuilder projectBuilder = mavenSession.getProjectBuilder();
    try {
        return projectBuilder.build(session.getCurrentProject().getBasedir()).getProject();
    } catch (ProjectBuildingException e) {
        throw new MojoExecutionException("Could not build project: " + e.getMessage(), e);
    }
}
```

This version of the method uses the `MavenSession` to get the `ProjectBuilder`, which can be used to build the `MavenProject` for the given basedir. This should work as a replacement for the original implementation that used the `MavenProject` directly.