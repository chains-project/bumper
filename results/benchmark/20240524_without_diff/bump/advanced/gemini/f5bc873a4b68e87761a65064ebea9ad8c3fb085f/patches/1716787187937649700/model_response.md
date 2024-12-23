```java
import org.apache.maven.execution.MavenSession;
import org.apache.maven.project.MavenProject;
import org.apache.maven.settings.Settings;

import java.io.File;

public abstract class AbstractThemeMojo extends AbstractMojo {

    @Parameter(defaultValue = "${session}", readonly = true)
    private MavenSession session;

    @Parameter(defaultValue = "${project}", readonly = true)
    private MavenProject project;

    @Parameter(defaultValue = "${settings}", readonly = true)
    private Settings settings;

    @Parameter(defaultValue = "${project.build.outputDirectory}", required = true)
    private File classesDirectory;

    @Parameter(defaultValue = "${project.build.testOutputDirectory}", required = true)
    private File testClassesDirectory;

    @Parameter(defaultValue = "${project.basedir}/src/main/resources", required = true)
    private File resourcesDirectory;

    @Parameter(defaultValue = "${project.basedir}/src/test/resources", required = true)
    private File testResourcesDirectory;

    @Parameter(defaultValue = "${project.build.directory}/site", required = true)
    private File siteDirectory;

    public MavenSession getSession() {
        return session;
    }

    public MavenProject getProject() {
        return project;
    }

    public Settings getSettings() {
        return settings;
    }

    public File getClassesDirectory() {
        return classesDirectory;
    }

    public File getTestClassesDirectory() {
        return testClassesDirectory;
    }

    public File getResourcesDirectory() {
        return resourcesDirectory;
    }

    public File getTestResourcesDirectory() {
        return testResourcesDirectory;
    }

    public File getSiteDirectory() {
        return siteDirectory;
    }
}
```