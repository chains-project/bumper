Here's the fixed `checkInputs` method:

```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl().toString(), server.getDistribution().getUrl().toString(),
            step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IOException("Server URL is missing");
    }
    if (isNotBlank(step.credentialsId)) {
        if (isNotBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```

The change is to call the `toString()` method on the `getUrl()` calls for the `Artifactory` and `Distribution` objects, since those objects have changed in the new library version. This ensures that the correct string representation is used in the `isAllBlank()` method call.