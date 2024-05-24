Here's the fixed version of the `checkInputs` method that should resolve the compilation error:

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

The only change here is the addition of the `toString()` method call for `server.getArtifactory().getUrl()` and `server.getDistribution().getUrl()`. This is because the `getUrl()` method now returns an instance of `P4ChangeEntry` or `P4GraphRef` instead of a `String`. By calling `toString()`, you'll get the actual URL string.