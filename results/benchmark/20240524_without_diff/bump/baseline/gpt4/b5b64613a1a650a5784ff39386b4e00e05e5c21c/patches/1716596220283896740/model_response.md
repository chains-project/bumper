```java
/**
     * Validate step's inputs.
     *
     * @param server - The server to check
     * @throws IOException if there is an illegal step configuration.
     */
    private void checkInputs(JFrogPlatformInstance server) throws IOException {
        if (server == null || step == null) {
            throw new IOException("Server or Step is null");
        }

        String serverUrl = server.getUrl();
        String artifactoryUrl = server.getArtifactory() != null ? server.getArtifactory().getUrl() : null;
        String distributionUrl = server.getDistribution() != null ? server.getDistribution().getUrl() : null;

        if (isAllBlank(serverUrl, artifactoryUrl, distributionUrl,
                step.url, step.artifactoryUrl, step.distributionUrl)) {
            throw new IOException("Server URL is missing");
        }
        if (isNotBlank(step.credentialsId)) {
            if (isNotBlank(step.username)) {
                throw new IOException("'rtServer' step can't include both credentialsId and username");
            }
            if (isNotBlank(step.password)) {
                throw new IOException("'rtServer' step can't include both credentialsId and password");
            }
        }
    }
```