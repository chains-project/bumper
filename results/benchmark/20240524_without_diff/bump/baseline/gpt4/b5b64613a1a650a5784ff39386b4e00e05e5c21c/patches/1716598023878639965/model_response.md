```java
/**
 * Validate step's inputs.
 *
 * @param server - The server to check
 * @throws IOException if there is an illegal step configuration.
 */
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
            this.step.getUrl(), this.step.getArtifactoryUrl(), this.step.getDistributionUrl())) {
        throw new IOException("Server URL is missing");
    }
    if (isNotBlank(this.step.getCredentialsId())) {
        if (isNotBlank(this.step.getUsername())) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (isNotBlank(this.step.getPassword())) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```