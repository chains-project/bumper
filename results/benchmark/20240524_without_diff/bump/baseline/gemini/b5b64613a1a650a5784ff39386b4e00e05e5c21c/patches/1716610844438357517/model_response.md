```java
        private void checkInputs(ArtifactoryServer server) throws IOException {
            if (isAllBlank(server.getUrl(), step.url)) {
                throw new IOException("Server URL is missing");
            }
            if (isNotBlank(step.credentialsId)) {
                if (isNotBlank(step.username) || isNotBlank(step.password)) {
                    throw new IOException("'rtServer' step can't include both credentialsId and username or password");
                }
            }
        }
```