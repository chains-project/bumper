```java
  /**
     * Generates SCoverage report.
     *
     * @throws MojoExecutionException if unexpected problem occurs
     */
    public void execute()
        throws MojoExecutionException
    {
        if ( !canGenerateReport() )
        {
            getLog().info( "Skipping SCoverage report generation" );
            return;
        }

        RenderingContext context = new RenderingContext( outputDirectory, getOutputName() + ".html" );
        SiteRendererSink sink = new SiteRendererSink( context );
        Locale locale = Locale.getDefault();
        generate( sink, locale );
    }
```