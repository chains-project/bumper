```java
import org.apache.maven.doxia.decoration.model.DecorationModel;
import org.apache.maven.doxia.sink.Sink;
import org.apache.maven.doxia.sink.SinkEventAttributes;
import org.apache.maven.doxia.sink.SinkEventElement;
import org.apache.maven.doxia.sink.SinkEventText;
import org.apache.maven.doxia.sink.SinkEventTextEvent;
import org.apache.maven.doxia.site.decoration.DecorationModelSource;
import org.apache.maven.doxia.siterenderer.Renderer;
import org.apache.maven.doxia.siterenderer.sink.SiteRendererSink;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.component.annotations.Component;
import org.codehaus.plexus.component.annotations.Requirement;
import org.codehaus.plexus.logging.Logger;
import org.codehaus.plexus.util.StringUtils;

import java.io.IOException;
import java.io.Writer;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 *
 *
 * @since 1.0
 */
@Component( role = Renderer.class, hint = "scoverage" )
public class SCoverageRenderer
    implements Renderer
{
    /**
     *
     */
    @Requirement
    private Logger logger;

    /**
     *
     */
    @Requirement
    private DecorationModelSource decorationModelSource;

    /**
     *
     */
    public String getOutputName()
    {
        return "scoverage";
    }

    /**
     * {@inheritDoc}
     */
    public void render( Sink sink, MavenProject project, Writer writer, Map<String, Object> context )
        throws IOException
    {
        // TODO: this is a hack, we should get the DecorationModel from the context
        DecorationModel model = decorationModelSource.getDecorationModel( "scoverage" );

        if ( model == null )
        {
            return;
        }

        Map<String, String> attributes = new HashMap<>();
        attributes.put( "class", "scoverage" );

        sink.head();
        sink.title();
        sink.text( "SCoverage" );
        sink.title_();
        sink.head_();

        sink.body();

        sink.section1();
        sink.sectionTitle1();
        sink.text( "SCoverage Report" );
        sink.sectionTitle1_();

        sink.paragraph();
        sink.text( "This report shows the code coverage for the current project." );
        sink.paragraph_();

        sink.section1_();

        sink.section2();
        sink.sectionTitle2();
        sink.text( "Summary" );
        sink.sectionTitle2_();

        sink.table();
        sink.tableRow();
        sink.tableHeaderCell();
        sink.text( "Metric" );
        sink.tableHeaderCell_();
        sink.tableHeaderCell();
        sink.text( "Value" );
        sink.tableHeaderCell_();
        sink.tableRow_();

        sink.tableRow();
        sink.tableCell();
        sink.text( "Lines of code" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( String.valueOf( (Integer) context.get( "lines" ) ) );
        sink.tableCell_();
        sink.tableRow_();

        sink.tableRow();
        sink.tableCell();
        sink.text( "Lines covered" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( String.valueOf( (Integer) context.get( "covered" ) ) );
        sink.tableCell_();
        sink.tableRow_();

        sink.tableRow();
        sink.tableCell();
        sink.text( "Coverage" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( String.valueOf( (Float) context.get( "coverage" ) ) + "%" );
        sink.tableCell_();
        sink.tableRow_();

        sink.table_();

        sink.section2_();

        sink.section2();
        sink.sectionTitle2();
        sink.text( "Details" );
        sink.sectionTitle2_();

        sink.paragraph();
        sink.text( "The following table shows the code coverage for each file." );
        sink.paragraph_();

        sink.table();
        sink.tableRow();
        sink.tableHeaderCell();
        sink.text( "File" );
        sink.tableHeaderCell_();
        sink.tableHeaderCell();
        sink.text( "Lines of code" );
        sink.tableHeaderCell_();
        sink.tableHeaderCell();
        sink.text( "Lines covered" );
        sink.tableHeaderCell_();
        sink.tableHeaderCell();
        sink.text( "Coverage" );
        sink.tableHeaderCell_();
        sink.tableRow_();

        List<Map<String, Object>> files = (List<Map<String, Object>>) context.get( "files" );
        for ( Map<String, Object> file : files )
        {
            sink.tableRow();
            sink.tableCell();
            sink.link( (String) file.get( "link" ), (String) file.get( "name" ) );
            sink.link_();
            sink.tableCell_();
            sink.tableCell();
            sink.text( String.valueOf( (Integer) file.get( "lines" ) ) );
            sink.tableCell_();
            sink.tableCell();
            sink.text( String.valueOf( (Integer) file.get( "covered" ) ) );
            sink.tableCell_();
            sink.tableCell();
            sink.text( String.valueOf( (Float) file.get( "coverage" ) ) + "%" );
            sink.tableCell_();
            sink.tableRow_();
        }

        sink.table_();

        sink.section2_();

        sink.body_();
    }
}
```