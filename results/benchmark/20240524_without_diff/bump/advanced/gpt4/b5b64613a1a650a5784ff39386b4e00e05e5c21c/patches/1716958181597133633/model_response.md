```java
/**
 * Validate step's inputs.
 *
 * @param server
 * 		- The server to check
 * @throws IOException
 * 		if there is an illegal step configuration.
 */
private void checkInputs(org.jfrog.hudson.pipeline.common.types.ArtifactoryServer server) throws java.io.IOException {
    if (server.getUrl() == null || server.getUrl().trim().isEmpty() || step.url == null || step.url.trim().isEmpty()) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (step.credentialsId != null && !step.credentialsId.trim().isEmpty()) {
        if (step.username != null && !step.username.trim().isEmpty()) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (step.password != null && !step.password.trim().isEmpty()) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```