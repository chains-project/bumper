```java
import org.apache.maven.doxia.sink.Sink;
import org.apache.maven.doxia.site.decoration.DecorationModel;
import org.apache.maven.project.MavenProject;
import org.apache.maven.reporting.MavenReportException;
import org.codehaus.plexus.util.StringUtils;
import org.scoverage.plugin.SCoverageUtils;

import java.io.File;
import java.io.IOException;
import java.util.Locale;

/**
 * Generates the Surefire report.
 *
 * @author <a href="mailto:jason@planet57.com">Jason Dillon</a>
 * @since 1.0
 */
public class SCoverageReportMojo
    extends AbstractSurefireMojo
{
    // ----------------------------------------------------------------------
    // Mojo Parameters
    // ----------------------------------------------------------------------

    /**
     * Directory where generated reports will be placed.
     *
     * @parameter expression="${project.reporting.outputDirectory}"
     * @required
     */
    private File outputDirectory;

    // ----------------------------------------------------------------------
    // Public methods
    // ----------------------------------------------------------------------

    /** {@inheritDoc} */
    public void execute()
        throws MavenReportException
    {
        if ( !canGenerateReport() )
        {
            return;
        }

        try
        {
            SCoverageUtils.writeSurefireReport( getLog(), getSurefireReportFile(), getReportOutputName(),
                                                 getReportOutputDirectory(), getProject(), getLocale() );
        }
        catch ( IOException e )
        {
            throw new MavenReportException( "Failed to write Surefire report: " + e.getMessage(), e );
        }
    }

    // ----------------------------------------------------------------------
    // Protected methods
    // ----------------------------------------------------------------------

    /**
     * @return The locale to use for generating the report
     */
    protected Locale getLocale()
    {
        return Locale.getDefault();
    }

    /**
     * @return The report output directory
     */
    protected File getReportOutputDirectory()
    {
        return outputDirectory;
    }

    /**
     * @return The name of the report output file
     */
    protected String getReportOutputName()
    {
        return "scoverage";
    }

    /**
     * @return The Surefire report file
     */
    protected File getSurefireReportFile()
    {
        String path = "target/surefire-reports";

        File reportFile = new File( getProject().getBasedir(), path );

        if ( reportFile.exists() )
        {
            File[] files = reportFile.listFiles();

            if ( files != null )
            {
                for ( File file : files )
                {
                    if ( file.getName().startsWith( "TEST-" ) && file.getName().endsWith( ".xml" ) )
                    {
                        return file;
                    }
                }
            }
        }

        return null;
    }

    // ----------------------------------------------------------------------
    // Private methods
    // ----------------------------------------------------------------------

    private boolean canGenerateReport()
    {
        // TODO: Make this configurable?
        return StringUtils.isNotEmpty( getReportOutputName() ) && getSurefireReportFile() != null;
    }
}
```