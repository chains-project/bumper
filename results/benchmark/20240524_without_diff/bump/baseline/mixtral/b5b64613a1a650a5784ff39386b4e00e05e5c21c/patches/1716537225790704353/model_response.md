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

The only change is that I added the `toString()` method on the `server.getArtifactory().getUrl()` and `server.getDistribution().getUrl()` calls since the `isAllBlank` method expects `String` arguments. The `getUrl()` method for the new library version returns a `java.lang.String`, but for the older version, it might return a different type, so to be safe, I added the `toString()` method.