```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingException;
import org.apache.maven.doxia.module.xhtml.decoration.render.Renderer;
import org.apache.maven.doxia.sink.Sink;
import org.apache.maven.doxia.siterenderer.RendererException;
import org.apache.maven.doxia.util.DoxiaUtils;
import org.codehaus.plexus.util.StringUtils;

import java.io.IOException;
import java.util.Locale;

/**
 * Renderer for the Doxia site report.
 *
 * @author <a href="mailto:vincent.siveton@gmail.com">Vincent Siveton</a>
 * @since 1.0
 */
public class DoxiaSiteRenderer
    implements Renderer
{
    /** The Doxia sink. */
    private Sink sink;

    /** The site renderer. */
    private final org.apache.maven.doxia.siterenderer.SiteRenderer siteRenderer;

    /** The locale. */
    private final Locale locale;

    /**
     * Creates the Doxia site renderer.
     *
     * @param sink        the Doxia sink.
     * @param siteRenderer the site renderer.
     * @param locale       the locale.
     */
    public DoxiaSiteRenderer( Sink sink, org.apache.maven.doxia.siterenderer.SiteRenderer siteRenderer, Locale locale )
    {
        this.sink = sink;
        this.siteRenderer = siteRenderer;
        this.locale = locale;
    }

    /**
     * {@inheritDoc}
     *
     * @see org.apache.maven.doxia.module.xhtml.decoration.render.Renderer#render()
     */
    public void render()
        throws RenderingException
    {
        try
        {
            siteRenderer.render( "site", locale, sink );
        }
        catch ( RendererException e )
        {
            throw new RenderingException( "Failed to render site", e );
        }
    }
}
```