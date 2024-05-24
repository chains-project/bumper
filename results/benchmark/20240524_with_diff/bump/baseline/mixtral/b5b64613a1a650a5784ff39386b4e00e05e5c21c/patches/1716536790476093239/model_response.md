Here's a fixed version of the `checkInputs` method that should resolve the compilation error:

```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (isAllBlank(server.getUrl(), Objects.requireNonNull(server.getArtifactory()).getUrl(), Objects.requireNonNull(server.getDistribution()).getUrl(),
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

The change here is the addition of `Objects.requireNonNull()` to ensure that the `getArtifactory()` and `getDistribution()` methods do not return `null`. This way, the `getUrl()` method can be called on the non-null objects, avoiding the compilation error.