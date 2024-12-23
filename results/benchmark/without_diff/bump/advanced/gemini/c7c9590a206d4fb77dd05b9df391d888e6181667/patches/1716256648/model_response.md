```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.sink.Sink;

public class SCoverageReportMojo extends AbstractReportMojo {

    /**
     * @component
     * @required
     * @readonly
     */
    private DoxiaSiteRenderer siteRenderer;

    /**
     * @parameter expression="${project}"
     * @required
     * @readonly
     */
    private MavenProject project;

    /**
     * @parameter expression="${component.org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext}"
     * @required
     */
    private RenderingContext renderingContext;

    /**
     * @parameter expression="${component.org.apache.maven.doxia.sink.Sink}"
     * @required
     */
    private Sink sink;

    @Override
    protected void executeReport(Locale locale) throws MojoExecutionException, MojoFailureException {
        try {
            // Get the Doxia site renderer.
            DoxiaSiteRenderer siteRenderer = getComponent(DoxiaSiteRenderer.class);

            // Get the Maven project.
            MavenProject project = (MavenProject) getPluginContext().get("project");

            // Get the rendering context.
            RenderingContext renderingContext = (RenderingContext) getPluginContext().get("renderingContext");

            // Get the sink.
            Sink sink = (Sink) getPluginContext().get("sink");

            // Generate the report.
            siteRenderer.generateDocument(sink, renderingContext);

        } catch (DoxiaException e) {
            throw new MojoExecutionException("An error occurred while generating the report.", e);
        }
    }
}
```