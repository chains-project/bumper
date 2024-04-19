Here's a proposed patch to fix the error in the provided code:
```
private void checkInputs(JFrogPlatformInstance server) throws IOException {
        if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
                step.url, step.artifactoryUrl, step.distributionUrl)) {
            throw new IOException("Server URL is missing");
        }
        if (!isBlank(step.credentialsId)) { // Modified line
            if (isNotBlank(step.username)) {
                throw new IOException("'rtServer' step can't include both credentialsId and username");
            }
            if (isNotBlank(step.password)) {
                throw new IOException("'rtServer' step can't include both credentialsId and password");
            }
        }
    }
```
The modification made was changing the condition `isNotBlank(step.credentialsId)` to `!isBlank(step.credentialsId)` to fix the error.
The `isBlank()` method is not recognized, and the `!` operator is used to negate the result of `isBlank()` to achieve the desired result.