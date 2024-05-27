Here's the patched version of the failing method:
```java
import org.apache.maven.model.Model;
import org.apache.maven.project.MavenProjectBuilder;

// ...

@Override
public void execute() throws MojoExecutionException {
    super.execute();

    MavenProject project = null;
    try {
        Model model = session.getProjectBuildingRequest().getOriginalModel();
        project = new MavenProjectBuilder().build(model);
    } catch (ProjectBuildingException e) {
        throw new MojoExecutionException("Failed to build Maven project", e);
    }

    // ...
}
```
In this patch, I replaced the usage of `MavenProject` with `org.apache.maven.project.MavenProjectBuilder` to build the `MavenProject` using the `Model` object. This is because the `MavenProject` constructor is no longer available in the updated library.