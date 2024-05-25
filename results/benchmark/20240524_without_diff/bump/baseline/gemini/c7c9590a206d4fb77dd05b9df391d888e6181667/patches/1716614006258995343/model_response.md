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

        try
        {
            RenderingContext context = new RenderingContext( outputDirectory, getOutputName() + ".html" );
            Locale locale = Locale.getDefault();
            SCoverageReportGenerator generator = new SCoverageReportGenerator();
            generator.generate(context, locale);
        }
        catch ( MavenReportException e )
        {
            String prefix = "An error has occurred in " + getName( Locale.ENGLISH ) + " report generation";
            throw new MojoExecutionException( prefix + ": " + e.getMessage(), e );
        }
    }
```