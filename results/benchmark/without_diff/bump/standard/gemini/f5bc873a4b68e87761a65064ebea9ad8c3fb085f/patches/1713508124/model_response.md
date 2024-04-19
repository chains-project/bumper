```java
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.project.MavenProject;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.plugins.annotations.Mojo;

import java.io.File;

@Mojo(name = "theme")
public class AbstractThemeMojo extends AbstractMojo {

    @Parameter(defaultValue = "${project}", readonly = true, required = true)
    protected MavenProject project;

    @Parameter(defaultValue = "${project.build.directory}/tobago-theme", required = true)
    protected File themeDirectory;

    @Parameter(defaultValue = "${project.build.directory}/classes", required = true)
    protected File classesDirectory;

    @Parameter(defaultValue = "${project.build.directory}/test-classes", required = true)
    protected File testClassesDirectory;

}
```