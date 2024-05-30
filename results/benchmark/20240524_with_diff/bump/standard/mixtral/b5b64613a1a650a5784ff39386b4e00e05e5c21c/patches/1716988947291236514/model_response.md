Here's the patched version of the `checkInputs` method:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), Objects.requireNonNullElse(server.getArtifactory(), "").getUrl(), Objects.requireNonNullElse(server.getDistribution(), "").getUrl(), Objects.requireNonNullElse(step.url, ""), Objects.requireNonNullElse(step.artifactoryUrl, ""), Objects.requireNonNullElse(step.distributionUrl, ""))) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (StringUtils.isNotBlank(step.credentialsId)) {
        if (StringUtils.isNotBlank(step.username)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (StringUtils.isNotBlank(step.password)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```

The patch includes adding `java.util.Objects` to check for null values and replace them with an empty string before calling `isAllBlank`. This ensures that the method call does not fail due to null values.