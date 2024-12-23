```java
import org.apache.maven.doxia.sink.Sink;
import org.apache.maven.reporting.MavenReportException;
import org.codehaus.plexus.util.StringUtils;

/**
 * @author <a href="mailto:joakim@erdfelt.com">Joakim Erdfelt</a>
 * @version $Id$
 */
public class SCoverageReportMojo
    extends AbstractScoverageReportMojo
{
    // ----------------------------------------------------------------------
    // Mojo Parameters
    // ----------------------------------------------------------------------

    /**
     * @parameter expression="${scoverage.outputDirectory}"
     * @required
     */
    private File outputDirectory;

    /**
     * @parameter expression="${scoverage.linkage}"
     * @required
     */
    private boolean linkage;

    /**
     * @parameter expression="${scoverage.linkage.includeScope}" default-value="test"
     * @required
     */
    private String linkageIncludeScope;

    /**
     * @parameter expression="${scoverage.linkage.excludeScope}" default-value=""
     * @required
     */
    private String linkageExcludeScope;

    /**
     * @parameter expression="${scoverage.linkage.title}" default-value="Linkage Coverage"
     * @required
     */
    private String linkageTitle;

    /**
     * @parameter expression="${scoverage.linkage.linkageReport}" default-value="linkage.html"
     * @required
     */
    private String linkageReport;

    /**
     * @parameter expression="${scoverage.linkage.excludePackages}" default-value=""
     * @required
     */
    private String linkageExcludePackages;

    /**
     * @parameter expression="${scoverage.linkage.excludeClasses}" default-value=""
     * @required
     */
    private String linkageExcludeClasses;

    /**
     * @parameter expression="${scoverage.linkage.excludeMethods}" default-value=""
     * @required
     */
    private String linkageExcludeMethods;

    /**
     * @parameter expression="${scoverage.linkage.excludeFields}" default-value=""
     * @required
     */
    private String linkageExcludeFields;

    /**
     * @parameter expression="${scoverage.linkage.excludeFields}" default-value=""
     * @required
     */
    private String linkageExcludeInnerClasses;

    /**
     * @parameter expression="${scoverage.linkage.excludeFields}" default-value=""
     * @required
     */
    private String linkageExcludeInnerEnums;

    /**
     * @parameter expression="${scoverage.linkage.excludeFields}" default-value=""
     * @required
     */
    private String linkageExcludeInnerInterfaces;

    /**
     * @parameter expression="${scoverage.linkage.excludeFields}" default-value=""
     * @required
     */
    private String linkageExcludeInnerAnnotations;

    // ----------------------------------------------------------------------
    // Public Methods
    // ----------------------------------------------------------------------

    /**
     * @see org.apache.maven.reporting.AbstractMavenReport#executeReport(org.apache.maven.reporting.MavenReportExecution)
     */
    public void executeReport( MavenReportExecution reportExecution )
        throws MavenReportException
    {
        if ( isSkip() )
        {
            return;
        }

        try
        {
            if ( getScoverageSession() == null )
            {
                getLog().info( "Skipping scoverage report generation. No scoverage session found." );
                return;
            }

            File outputDirectory = getOutputDirectory();
            if ( !outputDirectory.exists() )
            {
                if ( !outputDirectory.mkdirs() )
                {
                    throw new MavenReportException( "Unable to create report directory: " + outputDirectory );
                }
            }

            Sink sink = getSink();

            sink.head();
            sink.title();
            sink.text( "Scoverage Report" );
            sink.title_();
            sink.head_();

            sink.body();

            sink.section1();
            sink.sectionTitle1();
            sink.text( "Scoverage Report" );
            sink.sectionTitle1_();

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
            sink.text( "Covered Lines" );
            sink.tableCell_();
            sink.tableCell();
            sink.text( getScoverageSession().getCoveredLines() );
            sink.tableCell_();
            sink.tableRow_();

            sink.tableRow();
            sink.tableCell();
            sink.text( "Total Lines" );
            sink.tableCell_();
            sink.tableCell();
            sink.text( getScoverageSession().getTotalLines() );
            sink.tableCell_();
            sink.tableRow_();

            sink.tableRow();
            sink.tableCell();
            sink.text( "Coverage" );
            sink.tableCell_();
            sink.tableCell();
            sink.text( getScoverageSession().getCoverage() + "%" );
            sink.tableCell_();
            sink.tableRow_();

            sink.table_();

            sink.section2_();

            if ( linkage )
            {
                sink.section2();
                sink.sectionTitle2();
                sink.text( "Linkage Coverage" );
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
                sink.text( "Covered Packages" );
                sink.tableCell_();
                sink.tableCell();
                sink.text( getScoverageSession().getCoveredPackages() );
                sink.tableCell_();
                sink.tableRow_();

                sink.tableRow();
                sink.tableCell();
                sink.text( "Total Packages" );
                sink.tableCell_();
                sink.tableCell();
                sink.text( getScoverageSession().getTotalPackages() );
                sink.tableCell_();
                sink.tableRow_();

                sink.tableRow();
                sink.tableCell();
                sink.text( "Coverage" );
                sink.tableCell_();
                sink.tableCell();
                sink.text( getScoverageSession().getLinkageCoverage() + "%" );
                sink.tableCell_();
                sink.tableRow_();

                sink.table_();

                sink.section2_();

                if ( StringUtils.isNotEmpty( linkageReport ) )
                {
                    sink.section3();
                    sink.sectionTitle3();
                    sink.text( "Linkage Report" );
                    sink.sectionTitle3_();

                    sink.link( linkageReport );
                    sink.text( linkageTitle );
                    sink.link_();

                    sink.section3_();
                }
            }

            sink.section1_();

            sink.body_();

            sink.close();
        }
        catch ( Exception e )
        {
            throw new MavenReportException( "An error occurred while generating the scoverage report.", e );
        }
    }

    // ----------------------------------------------------------------------
    // Getters and Setters
    // ----------------------------------------------------------------------

    /**
     * @return the output directory
     */
    public File getOutputDirectory()
    {
        return outputDirectory;
    }

    /**
     * @param outputDirectory the output directory
     */
    public void setOutputDirectory( File outputDirectory )
    {
        this.outputDirectory = outputDirectory;
    }

    /**
     * @return true if linkage should be generated
     */
    public boolean isLinkage()
    {
        return linkage;
    }

    /**
     * @param linkage true if linkage should be generated
     */
    public void setLinkage( boolean linkage )
    {
        this.linkage = linkage;
    }

    /**
     * @return the scope to include for linkage
     */
    public String getLinkageIncludeScope()
    {
        return linkageIncludeScope;
    }

    /**
     * @param linkageIncludeScope the scope to include for linkage
     */
    public void setLinkageIncludeScope( String linkageIncludeScope )
    {
        this.linkageIncludeScope = linkageIncludeScope;
    }

    /**
     * @return the scope to exclude for linkage
     */
    public String getLinkageExcludeScope()
    {
        return linkageExcludeScope;
    }

    /**
     * @param linkageExcludeScope the scope to exclude for linkage
     */
    public void setLinkageExcludeScope( String linkageExcludeScope )
    {
        this.linkageExcludeScope = linkageExcludeScope;
    }

    /**
     * @return the title of the linkage report
     */
    public String getLinkageTitle()
    {
        return linkageTitle;
    }

    /**
     * @param linkageTitle the title of the linkage report
     */
    public void setLinkageTitle( String linkageTitle )
    {
        this.linkageTitle = linkageTitle;
    }

    /**
     * @return the filename of the linkage report
     */
    public String getLinkageReport()
    {
        return linkageReport;
    }

    /**
     * @param linkageReport the filename of the linkage report
     */
    public void setLinkageReport( String linkageReport )
    {
        this.linkageReport = linkageReport;
    }

    /**
     * @return the packages to exclude from linkage
     */
    public String getLinkageExcludePackages()
    {
        return linkageExcludePackages;
    }

    /**
     * @param linkageExcludePackages the packages to exclude from linkage
     */
    public void setLinkageExcludePackages( String linkageExcludePackages )
    {
        this.linkageExcludePackages = linkageExcludePackages;
    }

    /**
     * @return the classes to exclude from linkage
     */
    public String getLinkageExcludeClasses()
    {
        return linkageExcludeClasses;
    }

    /**
     * @param linkageExcludeClasses the classes to exclude from linkage
     */
    public void setLinkageExcludeClasses( String linkageExcludeClasses )
    {
        this.linkageExcludeClasses = linkageExcludeClasses;
    }

    /**
     * @return the methods to exclude from linkage
     */
    public String getLinkageExcludeMethods()
    {
        return linkageExcludeMethods;
    }

    /**
     * @param linkageExcludeMethods the methods to exclude from linkage
     */
    public void setLinkageExcludeMethods( String linkageExcludeMethods )
    {
        this.linkageExcludeMethods = linkageExcludeMethods;
    }

    /**
     * @return the fields to exclude from linkage
     */
    public String getLinkageExcludeFields()
    {
        return linkageExcludeFields;
    }

    /**
     * @param linkageExcludeFields the fields to exclude from linkage
     */
    public void setLinkageExcludeFields( String linkageExcludeFields )
    {
        this.linkageExcludeFields = linkageExcludeFields;
    }

    /**
     * @return the inner classes to exclude from linkage
     */
    public String getLinkageExcludeInnerClasses()
    {
        return linkageExcludeInnerClasses;
    }

    /**
     * @param linkageExcludeInnerClasses the inner classes to exclude from linkage
     */
    public void setLinkageExcludeInnerClasses( String linkageExcludeInnerClasses )
    {
        this.linkageExcludeInnerClasses = linkageExcludeInnerClasses;
    }

    /**
     * @return the inner enums to exclude from linkage
     */
    public String getLinkageExcludeInnerEnums()
    {
        return linkageExcludeInnerEnums;
    }

    /**
     * @param linkageExcludeInnerEnums the inner enums to exclude from linkage
     */
    public void setLinkageExcludeInnerEnums( String linkageExcludeInnerEnums )
    {
        this.linkageExcludeInnerEnums = linkageExcludeInnerEnums;
    }

    /**
     * @return the inner interfaces to exclude from linkage
     */
    public String getLinkageExcludeInnerInterfaces()
    {
        return linkageExcludeInnerInterfaces;
    }

    /**
     * @param linkageExcludeInnerInterfaces the inner interfaces to exclude from linkage
     */
    public void setLinkageExcludeInnerInterfaces( String linkageExcludeInnerInterfaces )
    {
        this.linkageExcludeInnerInterfaces = linkageExcludeInnerInterfaces;
    }

    /**
     * @return the inner annotations to exclude from linkage
     */
    public String getLinkageExcludeInnerAnnotations()
    {
        return linkageExcludeInnerAnnotations;
    }

    /**
     * @param linkageExcludeInnerAnnotations the inner annotations to exclude from linkage
     */
    public void setLinkageExcludeInnerAnnotations( String linkageExcludeInnerAnnotations )
    {
        this.linkageExcludeInnerAnnotations = linkageExcludeInnerAnnotations;
    }
}
```