```java
  /**
         * Validate step's inputs.
         *
         * @param server - The server to check
         * @throws IOException if there is an illegal step configuration.
         */
        private void checkInputs(JFrogPlatformInstance server) throws IOException {
            if (isBlank(server.getUrl()) && isBlank(server.getArtifactory().getUrl()) && isBlank(server.getDistribution().getUrl())
                    && isBlank(step.url) && isBlank(step.artifactoryUrl) && isBlank(step.distributionUrl)) {
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