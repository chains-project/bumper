Here is a patch that you can apply to the code in order to fix the error:

```java
import org.apache.maven.artifact.resolver.ArtifactResolutionException;

//...

@Override
public void execute() throws MojoExecutionException {
  try {
    //...
  } catch (ArtifactResolutionException e) {
    throw new MojoExecutionException("Failed to unpack theme", e);
  }
}
```

In the new version of the library, the `DependencyResolutionRequiredException` class has been removed and replaced with the `ArtifactResolutionException` class. Therefore, you can simply replace the former with the latter in the `execute` method. Additionally, you can remove the `throws DependencyResolutionRequiredException` clause from the method signature, as it is no longer needed.