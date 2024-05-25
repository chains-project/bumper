```java
/**
         * Validate step's inputs.
         *
         * @param server - The server to check
         * @throws IOException if there is an illegal step configuration.
         */
        private void checkInputs(JFrogPlatformInstance server) throws IOException {
            if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
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
            } else {
                if (isNotBlank(step.username) && isNotBlank(step.password)) {
                    // Use provided username and password
                } else {
                    // Use credentialsId to retrieve username and password
                    Credentials credentials = CredentialsMatchers.firstOrNull(
                            hudson.plugins.sshslaves.verifiers.NonInteractiveUsernamePasswordCredentialsImpl.class,
                            server.getCredentialsId(), hudson.model.Item.class, step, step.getDescriptor().isUseSecretToken());
                    if (credentials == null) {
                        throw new IOException("CredentialsId '" + server.getCredentialsId() + "' not found");
                    }
                    step.username = credentials.getUsername();
                    step.password = credentials.getPassword().getSecret();
                }
            }
        }
```