```java
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingContext;
import org.apache.maven.doxia.module.xhtml.decoration.render.RenderingException;
import org.apache.maven.doxia.sink.Sink;
import org.apache.maven.doxia.sink.SinkEventAttributes;

import java.util.Map;

/**
 * Renders the coverage report.
 *
 * @author <a href="mailto:jason@planet57.com">Jason Dillon</a>
 * @since 1.1
 */
public class SCoverageReportRenderer
{
    private final RenderingContext context;

    public SCoverageReportRenderer( final RenderingContext context )
    {
        this.context = context;
    }

    public void render( final SCoverageReport report )
        throws RenderingException
    {
        final Sink sink = context.getSink();

        sink.head();
        sink.title();
        sink.text( "SCoverage Report" );
        sink.title_();
        sink.head_();

        sink.body();

        sink.section1();
        sink.sectionTitle1();
        sink.text( "Summary" );
        sink.sectionTitle1_();

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
        sink.text( "Lines Covered" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( report.getLinesCovered() );
        sink.tableCell_();
        sink.tableRow_();

        sink.tableRow();
        sink.tableCell();
        sink.text( "Lines Missed" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( report.getLinesMissed() );
        sink.tableCell_();
        sink.tableRow_();

        sink.tableRow();
        sink.tableCell();
        sink.text( "Branches Covered" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( report.getBranchesCovered() );
        sink.tableCell_();
        sink.tableRow_();

        sink.tableRow();
        sink.tableCell();
        sink.text( "Branches Missed" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( report.getBranchesMissed() );
        sink.tableCell_();
        sink.tableRow_();

        sink.tableRow();
        sink.tableCell();
        sink.text( "Total Coverage" );
        sink.tableCell_();
        sink.tableCell();
        sink.text( report.getTotalCoverage() );
        sink.tableCell_();
        sink.tableRow_();

        sink.table_();

        sink.section1_();

        sink.section1();
        sink.sectionTitle1();
        sink.text( "Source Files" );
        sink.sectionTitle1_();

        sink.list();

        for ( final SCoverageSourceFile sourceFile : report.getSourceFiles() )
        {
            sink.listItem();
            sink.link( sourceFile.getLink(), sourceFile.getLink() );
            sink.text( sourceFile.getName() );
            sink.link_();
            sink.listItem_();
        }

        sink.list_();

        sink.section1_();

        sink.body_();
    }
}
```