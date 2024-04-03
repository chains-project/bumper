Here's the proposed patch to fix the error:

```java
import org.apache.maven.artifact.resolver.ArtifactResolutionException;

--

@Override
public void execute() throws MojoExecutionException, ArtifactResolutionException {
  // existing code
}
```

In this patch, we import the new `ArtifactResolutionException` class, which has replaced `DependencyResolutionRequiredException` in the updated library. We then replace the old exception class with the new one in the method signature. This should fix the "cannot find symbol" error.