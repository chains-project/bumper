Here's the proposed patch:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(), getStepUrl(), getStepArtifactoryUrl(), getStepDistributionUrl())) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (org.apache.commons.lang3.StringUtils.isNotBlank(getStepCredentialsId())) {
        if (org.apache.commons.lang3.StringUtils.isNotBlank(getStepUsername())) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (org.apache.commons.lang3.StringUtils.isNotBlank(getStepPassword())) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

private String getStepUrl() {
    return step.url;
}

private String getStepArtifactoryUrl() {
    return step.artifactoryUrl;
}

private String getStepDistributionUrl() {
    return step.distributionUrl;
}

private String getStepCredentialsId() {
    return step.credentialsId;
}

private String getStepUsername() {
    return step.username;
}

private String getStepPassword() {
    return step.password;
}
```

The changes made include creating new methods to extract the values from the `step` object and replace the direct access to the `step` object with the new methods. This way, the code can still work even if the `step` object changes in the future. Additionally, the `isAllBlank` method is assumed to be defined elsewhere in the codebase, so it is not modified here.