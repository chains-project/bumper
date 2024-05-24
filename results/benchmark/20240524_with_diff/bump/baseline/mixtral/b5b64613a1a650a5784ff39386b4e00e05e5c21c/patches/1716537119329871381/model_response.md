Here's a fixed version of the `checkInputs` method that should resolve the compilation error:

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

The change I made is to call the `toString()` method on the `getUrl()` calls for `server.getArtifactory()` and `server.getDistribution()`. This is because the `getUrl()` method was removed and replaced with a method that returns a `P4ChangeEntry` object. By calling `toString()` on this object, we convert it to a string, which should be compatible with the expected input of the `isAllBlank` method.