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
        String stepUrl = step.url;
        String stepArtifactoryUrl = step.artifactoryUrl;
        String stepDistributionUrl = step.distributionUrl;
        String stepCredentialsId = step.credentialsId;
        String stepUsername = step.username;
        String stepPassword = step.password;

        if (isAllBlank(serverUrl, artifactoryUrl, distributionUrl, stepUrl, stepArtifactoryUrl, stepDistributionUrl)) {
            throw new IOException("Server URL is missing");
        }
        if (isNotBlank(stepCredentialsId)) {
            if (isNotBlank(stepUsername)) {
                throw new IOException("'rtServer' step can't include both credentialsId and username");
            }
            if (isNotBlank(stepPassword)) {
                throw new IOException("'rtServer' step can't include both credentialsId and password");
            }
        }
    }
```