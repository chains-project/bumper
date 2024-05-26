Here is a patch that fixes the illegal character error:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl() != null ? server.getUrl() : "", server.getArtifactory() != null ? server.getArtifactory().getUrl() : "", server.getDistribution() != null ? server.getDistribution().getUrl() : "", step.url != null ? step.url : "", step.artifactoryUrl != null ? step.artifactoryUrl : "", step.distributionUrl != null ? step.distributionUrl : "")) {
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
```

This patch simply removes the offending character ` from the code. It is unclear where this character came from, but it is not a valid character in Java code.