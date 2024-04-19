Here's the fixed `unpackTheme` method with the required import statement:

```java
import org.eclipse.aether.resolution.ArtifactResolutionException;

@Override
public void unpackTheme(Theme theme, File outputDirectory) throws MojoExecutionException {
    try {
        // ... (existing code)
    } catch (ArtifactResolutionException e) {
        throw new MojoExecutionException("Unable to unpack theme " + theme.getId() + ": " + e.getMessage(), e);
    }
}
```

The `DependencyResolutionRequiredException` has been replaced by `ArtifactResolutionException` in the new version of the library.