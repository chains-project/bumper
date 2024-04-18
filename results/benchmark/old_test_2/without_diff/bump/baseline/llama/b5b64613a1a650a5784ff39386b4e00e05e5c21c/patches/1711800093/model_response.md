Here's a proposed patch to fix the error in the provided code:
```
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
        if (isNotBlank(step.username) && isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both username and password");
        }
    }
```
The patch removes the `isNotBlank()` method call for the `credentialsId` and `password` fields, as it is not necessary to check if they are not blank when checking if they are blank. Instead, we can directly check if they are blank or not.
Additionally, the patch removes the `Override` annotation as it is not needed in this method.
It is important to note that this patch only fixes the provided code snippet and it's possible that there are other issues in the complete code.