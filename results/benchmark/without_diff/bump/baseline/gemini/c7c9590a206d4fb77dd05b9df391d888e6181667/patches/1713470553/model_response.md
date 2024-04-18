```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingException;
import org.apache.maven.doxia.sink.Sink;
import org.apache.maven.reporting.MavenReportException;

import java.io.IOException;

/**
 * Renders the coverage report.
 *
 * @author <a href="mailto:joakim@erdfelt.com">Joakim Erdfelt</a>
 * @since 2.0
 */
public class SCoverageReportMojo
    extends AbstractSCoverageMojo
{

    // --++
    /**
     * Execute the mojo.
     *
     * @throws MavenReportException if any
     */
    protected void executeReport( Locale locale )
        throws MavenReportException
    {
        try
        {
            SCoverageReportGenerator reportGenerator = new SCoverageReportGenerator( getLog() );
            reportGenerator.setConfiguration( getConfiguration() );
            reportGenerator.setReportOutputDirectory( getOutputDirectory() );

            SCoverageResults results = getResults();

            if ( results != null )
            {
                reportGenerator.setResults( results );

                // --
                RenderingContext context = new RenderingContext();
                context.setSink( getSink() );
                context.setLocale( locale );

                reportGenerator.generate( context );
            }
        }
        catch ( IOException e )
        {
            throw new MavenReportException( "An error occurred while generating the coverage report: " + e.getMessage(),
                                             e );
        }
        catch ( RenderingException e )
        {
            throw new MavenReportException( "An error occurred while rendering the coverage report: " + e.getMessage(),
                                             e );
        }
    }

    // --++
    /**
     * {@inheritDoc}
     */
    protected Sink getSink()
    {
        return getSinkFactory().createSink( getOutputDirectory(), locale );
    }

}
```