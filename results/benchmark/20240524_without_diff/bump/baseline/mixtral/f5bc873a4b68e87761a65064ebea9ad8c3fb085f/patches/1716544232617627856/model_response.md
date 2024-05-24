Here is a possible patch for the failing method in the client code:
```java
try {
    artifactResolver.resolve(requestContext, artifact);
} catch (ArtifactResolveException e) {
    throw new MojoExecutionException("Failed to resolve artifact", e);
}
```
Note that I replaced the deprecated method `resolveTransitively` with the recommended method `resolve`. I also added a try-catch block to handle the new exception `ArtifactResolveException` that is thrown by the new method. This should fix the compilation error and make the code compatible with the new library version.