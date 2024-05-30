Here's a proposed patch for the failing client code:
```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), getArtifactoryUrl(server), getDistributionUrl(server), step.url, step.artifactoryUrl, step.distributionUrl)) {
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

private String getArtifactoryUrl(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) {
    return server.getArtifactory() != null ? server.getArtifactory().getUrl() : "";
}

private String getDistributionUrl(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) {
    return server.getDistribution() != null ? server.getDistribution().getUrl() : "";
}
```
I created two helper methods `getArtifactoryUrl` and `getDistributionUrl` to extract the URLs from the `JFrogPlatformInstance` object. This way, we can avoid calling the methods `getArtifactory().getUrl()` and `getDistribution().getUrl()` directly in the `isAllBlank` method call.

Also, I assumed that the `isAllBlank` method is a utility method that checks if all the provided strings are blank or not. If it's not the case, you might need to adjust the method accordingly.