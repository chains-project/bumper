```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.ProjectBuilder;

public abstract class AbstractThemeMojo extends AbstractMojo {

    @Parameter(defaultValue = "${project}", readonly = true, required = true)
    private MavenProject project;
    @Component
    private ProjectBuilder projectBuilder;

    @Override
    public void execute() throws MojoExecutionException, MojoFailureException {
        // Get the current project.
        MavenProject project = this.project;

        // Get the project builder.
        ProjectBuilder projectBuilder = this.projectBuilder;

        // Build the project.
        project = projectBuilder.build(project, session.getCurrentProjectLocator());

        // Set the project.
        this.project = project;

        // Execute the mojo.
        super.execute();
    }
}
```