```java
    @Override
    public void execute()
        throws MojoExecutionException
    {
        if ( !canGenerateReport() )
        {
            getLog().info( "Skipping SCoverage report generation" );
            return;
        }

        SiteRendererSink sink = null;
        RenderingContext context = null;
        try
        {
            context = new RenderingContext( outputDirectory, getOutputName() + ".html" );
            sink = new SiteRendererSink( context );
            Locale locale = Locale.getDefault();
            generate( sink, locale );
        }
        catch ( MavenReportException e )
        {
            String prefix = "An error has occurred in " + getName( Locale.ENGLISH ) + " report generation";
            throw new MojoExecutionException( prefix + ": " + e.getMessage(), e );
        }
        finally
        {
            if ( sink != null )
            {
                sink.close();
            }
            if ( context != null )
            {
                context.close();
            }
        }
    }
```