```java
    public void execute()
        throws MojoExecutionException
    {
        if ( !canGenerateReport() )
        {
            getLog().info( "Skipping SCoverage report generation" );
            return;
        }

        try
        {
            SiteRendererSink sink = new SiteRendererSink( new RenderingContext( outputDirectory, getOutputName() + ".html" ) );
            generate( sink, Locale.getDefault() );
        }
        catch ( MavenReportException e )
        {
            String prefix = "An error has occurred in " + getName( Locale.ENGLISH ) + " report generation";
            throw new MojoExecutionException( prefix + ": " + e.getMessage(), e );
        }
    }
```