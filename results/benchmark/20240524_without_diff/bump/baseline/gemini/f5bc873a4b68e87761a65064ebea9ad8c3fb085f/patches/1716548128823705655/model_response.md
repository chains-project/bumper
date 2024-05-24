```java
import org.apache.maven.artifact.resolver.ArtifactResolutionException;

  // ...

  try {
    // ...
  } catch (ArtifactResolutionException e) {
    throw new DependencyResolutionRequiredException(e.getMessage(), e);
  }

  // ...
```