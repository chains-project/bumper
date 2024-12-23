```java
/**
     * Validate step's inputs.
     *
     * @param server - The server to check
     * @throws IOException if there is an illegal step configuration.
     */
    private void checkInputs(ArtifactoryServer server) throws IOException {
        if (StringUtils.isAllBlank(server.getUrl(), step.getUrl())) {
            throw new IOException("Server URL is missing");
        }
        if (StringUtils.isNotBlank(step.getCredentialsId())) {
            if (StringUtils.isNotBlank(step.getUsername())) {
                throw new IOException("'rtServer' step can't include both credentialsId and username");
            }
            if (StringUtils.isNotBlank(step.getPassword())) {
                throw new IOException("'rtServer' step can't include both credentialsId and password");
            }
        }
    }
```