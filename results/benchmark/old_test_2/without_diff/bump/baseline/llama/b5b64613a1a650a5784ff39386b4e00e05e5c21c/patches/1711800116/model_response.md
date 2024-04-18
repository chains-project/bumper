Here's a proposed patch to fix the error in the provided code:
```java
private void checkInputs(ArtifactoryServer server) throws IOException {
        if (isAllBlank(server.getUrl(), step.url)) {
            throw new IOException("Server URL is missing");
        }
        if (!isBlank(step.credentialsId) && !isBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }

        if (!isBlank(step.credentialsId) && !isBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
```
The patch removes the `isNotBlank()` method call, which is not available in the dependencies of the project, and replaces it with `!isBlank()`, which is available in the same dependencies.