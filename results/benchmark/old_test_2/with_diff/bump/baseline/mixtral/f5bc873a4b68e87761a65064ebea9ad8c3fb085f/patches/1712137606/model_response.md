Here's the proposed patch for the failing method:

```java
import org.apache.maven.artifact.ResolverException;

...

@Override
public void execute() throws MojoExecutionException, MojoFailureException {
  try {
    // Your existing code here
  } catch (final Exception e) {
    throw new MojoExecutionException("Unable to unpack theme", e);
  }
}
```

The `DependencyResolutionRequiredException` class has been removed in the new library version. Instead, you can use the more general `ResolverException` class, which is a superclass of `DependencyResolutionRequiredException`. By catching `Exception`, you can handle any exceptions that might be thrown during execution and rethrow them as a more specific `MojoExecutionException`.