```java
/**
 * Validate step's inputs.
 *
 * @param server
 * 		- The server to check
 * @throws IOException
 * 		if there is an illegal step configuration.
 */
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (org.apache.commons.lang3.StringUtils.isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(), step.url, step.artifactoryUrl, step.distributionUrl)) {
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