Here's the fixed `checkInputs` method with the new library version:

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

The only change made is converting the `getUrl()` calls for `server.getArtifactory()` and `server.getDistribution()` to `getUrl().toString()` because the new version of the library returns an object implementing the `CharSequence` interface, and a `toString()` call is required for the `isAllBlank()` method.