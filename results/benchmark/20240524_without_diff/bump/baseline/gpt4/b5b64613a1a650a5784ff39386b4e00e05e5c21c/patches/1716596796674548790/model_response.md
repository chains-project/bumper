```java
/**
     * Validate step's inputs.
     *
     * @param server - The server to check
     * @throws IOException if there is an illegal step configuration.
     */
    private void checkInputs(JFrogPlatformInstance server) throws IOException {
        String serverUrl = server.getUrl();
        String artifactoryUrl = server.getArtifactory().getUrl();
        String distributionUrl = server.getDistribution().getUrl();

        if (isAllBlank(serverUrl, artifactoryUrl, distributionUrl,
                step.url, step.artifactoryUrl, step.distributionUrl)) {
            throw new IOException("Server URL is missing");
        }
        String credentialsId = step.credentialsId;
        if (isNotBlank(credentialsId)) {
            String username = step.username;
            if (isNotBlank(username)) {
                throw new IOException("'rtServer' step can't include both credentialsId and username");
            }
            String password = step.password;
            if (isNotBlank(password)) {
                throw new IOException("'rtServer' step can't include both credentialsId and password");
            }
        }
    }
```