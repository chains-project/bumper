Here's the patched method with the `isAllBlank` method implemented using `java.util.Objects.requireNonNullElse`:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(), step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (org.apache.commons.lang3.StringUtils.isNotBlank(step.credentialsId)) {
        if (org.apache.commons.lang3.StringUtils.isNotBlank(step.username)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (org.apache.commons.lang3.StringUtils.isNotBlank(step.password)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

private boolean isAllBlank(String url1, String url2, String url3, String stepUrl, String stepArtifactoryUrl, String stepDistributionUrl) {
    return Objects.requireNonNullElse(url1, "").isBlank()
        && Objects.requireNonNullElse(url2, "").isBlank()
        && Objects.requireNonNullElse(url3, "").isBlank()
        && Objects.requireNonNullElse(stepUrl, "").isBlank()
        && Objects.requireNonNullElse(stepArtifactoryUrl, "").isBlank()
        && Objects.requireNonNullElse(stepDistributionUrl, "").isBlank();
}
```

The new `isAllBlank` method checks if all the given strings are blank or not using `java.util.Objects.requireNonNullElse` to replace null values with an empty string before checking for blankness.