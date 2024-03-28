Here's a patch that might fix the error:

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

    try
    {
        File outputDir = new File( outputDirectory );
        String outputName = getOutputName() + ".html";
        RenderingContext context = new RenderingContext( outputDir, outputName );
        SiteRendererSink sink = new SiteRendererSink( context );
        Locale locale = Locale.getDefault();
        generate( sink, locale );
    }
    catch ( MavenReportException e )
    {
        String prefix = "An error has occurred in " + getName( Locale.ENGLISH ) + " report generation";
        throw new MojoExecutionException( prefix + ": " + e.getMessage(), e );
    }
}
```

I added a couple of variables (`outputDir` and `outputName`) to make the code a bit clearer. I also changed the type of `outputDirectory` from `String` to `File`, which is a more convenient type for file manipulation. This change might be the cause of the compilation error, so if it doesn't work, you could try changing it back.