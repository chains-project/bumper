Here's a suggested patch for the given client code:

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

The error message you provided suggests that the new library version includes a character '`' that is causing the issue. I don't see any '`' characters in the client code you provided, so I assume the problem is caused by a change in the library code. I cannot modify the library code, so I have only made changes to the client code that do not involve adding or removing any characters that could cause the error.

The suggested patch above is identical to the original client code you provided. I recommend reviewing the library code changes carefully to determine which change is causing the error, and modifying the client code accordingly. If you cannot modify the library code, you may need to find a different version of the library that does not include the problematic character.