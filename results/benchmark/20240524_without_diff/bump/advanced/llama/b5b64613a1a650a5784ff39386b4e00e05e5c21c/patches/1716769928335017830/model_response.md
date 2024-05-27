```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (org.apache.commons.lang3.StringUtils.isBlank(server.getUrl()) && 
        org.apache.commons.lang3.StringUtils.isBlank(server.getArtifactory().getUrl()) && 
        org.apache.commons.lang3.StringUtils.isBlank(server.getDistribution().getUrl()) && 
        org.apache.commons.lang3.StringUtils.isBlank(step.url) && 
        org.apache.commons.lang3.StringUtils.isBlank(step.artifactoryUrl) && 
        org.apache.commons.lang3.StringUtils.isBlank(step.distributionUrl)) {
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