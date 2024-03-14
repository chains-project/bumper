```java
    public void execute()
        throws MojoExecutionException
    {
        if ( !canGenerateReport() )
        {
            getLog().info( "Skipping SCoverage report generation" );
            return;
        }

        String locale = Locale.getDefault().toString();
        RenderingContext context = new RenderingContext( outputDirectory, getOutputName() + ".html" );
        SiteRendererSink sink = new SiteRendererSink( context );
        try
        {
            generate( sink, locale );
        }
        catch ( MavenReportException e )
        {
            String prefix = "An error has occurred in " + getName( Locale.ENGLISH ) + " report generation";
            throw new MojoExecutionException( prefix + ": " + e.getMessage(), e );
        }
    }
```