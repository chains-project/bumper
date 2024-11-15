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
            String stepCredentialsId = step.credentialsId;
            if (isNotBlank(stepCredentialsId)) {
                String stepUsername = step.username;
                if (isNotBlank(stepUsername)) {
                    throw new IOException("'rtServer' step can't include both credentialsId and username");
                }
                String stepPassword = step.password;
                if (isNotBlank(stepPassword)) {
                    throw new IOException("'rtServer' step can't include both credentialsId and password");
                }
            }
        }
```