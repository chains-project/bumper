Here's a possible patch for the `checkInputs` method that fixes the compilation error:

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

The change I made is to call the `toString()` method on the `getUrl()` method of the `Artifactory` and `Distribution` objects, since the `isAllBlank` method expects a `String` argument. I assumed that the `getUrl()` method of those objects returns a non-null value, since the original code didn't check for null. If this assumption is incorrect, you may need to add null checks.