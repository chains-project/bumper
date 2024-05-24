Here's the updated `checkInputs` method with the necessary changes to fix the compilation error:

```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    String url = server.getUrl();
    String artifactoryUrl = server.getArtifactory().getUrl();
    String distributionUrl = server.getDistribution().getUrl();
    String stepUrl = step.url;
    String stepArtifactoryUrl = step.artifactoryUrl;
    String stepDistributionUrl = step.distributionUrl;

    if (isAllBlank(url, artifactoryUrl, distributionUrl, stepUrl, stepArtifactoryUrl, stepDistributionUrl)) {
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

The changes include declaring the variables for each method call on the `JFrogPlatformInstance` and `Step` objects. This way, the `isAllBlank` method receives the correct number of arguments.