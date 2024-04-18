```
        private void checkInputs(ArtifactoryServer server) throws IOException {
            if (isAllBlank(server.getUrl(), step.url)) {
                throw new IOException("Server URL is missing");
            }
            if (!String.isBlank(step.credentialsId) && (isNotBlank(step.username) || isNotBlank(step.password))) {
                throw new IOException("'rtServer' step can't include both credentialsId and username or password");
            }
        }
```
In this patch, we've changed the condition in the second if statement to check if `credentialsId` is not blank and either `username` or `password` is not blank. This should fix the error and allow the code to compile.

Note that we've also removed the `Override` annotation, as it's not needed in this case.