Here's the proposed patch for the failing method in the client code:

```java
try {
    Artifact artifact = resolver.resolveArtifact(repositorySystemSession, artifactRequest);
    artifact.getFile();
} catch (ArtifactResolutionException e) {
    throw new MojoExecutionException("Unable to resolve artifact", e);
}
```

I made the following changes:

* Removed the unnecessary type declaration in the `artifactRequest` variable declaration.
* Replaced the deprecated method `resolveArtifact(...)` with the recommended `resolveArtifact(...)` method that returns an `Artifact` object.
* Added a call to the `getFile()` method of the `Artifact` object to force the download of the artifact.
* Wrapped the `ArtifactResolutionException` in a `MojoExecutionException` to preserve the original behavior of the method.